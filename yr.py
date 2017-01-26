# encoding: utf-8

import re
import sys
from lazy import Lazy
from urllib import urlopen
from datetime import datetime, timedelta


def fetch_source(url, timestamp = ""):
	'''
	Return a string containing the HTML source file of the webpage 'url'.
	Optional: Pass a timestamp and this overwrites the current time in Lazy.

	'''

	cache = Lazy(url_to_string, timestamp)
	return cache(url)


def url_to_string(url):
	'''
	Combines opening and reading of file info one function so that it can be
	used in conjunction with the custom Lazy evaluation class.

	'''

	url_obj = urlopen(url)

	try:
		content = url_obj.read()
		url_obj.close()
		return content
	except IOError as e:
		sys.exit(1)


def get_weather_url(location):
	''' Task 4.2
	Return a list of url strings pointing to Yrs
	weather data on the given'location'.

	'''

	data = fetch_source("http://fil.nrk.no/yr/viktigestader/noreg.txt")

	# If 'location' is empty, return all places.
	if (location) == "":
		return re.findall(r"http[^\t]*forecast.xml", data)

	# Support for regex syntax - any character(s) in place of a wildcard.
	loc_regex = location.replace("*", r"[^\t]*")

	# Try finding a matching "Stadnamn".
	pattern = r"\n\d+\t" + loc_regex + r"\t.*(http.*forecast.xml)"
	result = re.findall(pattern, data, re.IGNORECASE)

	# If no matching place is found, try the municipality.
	if not result:
		pattern = loc_regex + r"\t\w*\t\d.*(http.*forecast.xml)"
		result = re.findall(pattern, data, re.IGNORECASE)

	# If no matching municipality is found, try the county.
	if not result:
		pattern = loc_regex + r"\t\d.*(http.*forecast.xml)"
		result = re.findall(pattern, data, re.IGNORECASE)

	return result


def retrieve_weather_report(location):
	'''
	Return weather report(s) on passed location. Information is fetched from
	yr.no. Return value is a dictionary with location names for key and a table
	of various weather information for values. Uses nine regexes per URL.

	'''

	# List of (keyword, value) tuples used to search for data in the XML files.
	tags = [("time", "from"), ("time", "to"), ("temperature", "value"),
			("symbol", "name"), ("precipitation", "value"),
			("windSpeed", "name"), ("windSpeed", "mps")]

	urls = get_weather_url(location)

	# Limit to maximum 100 requests.
	if len(urls) > 100:
		urls = urls[0:101]

	# Create a dictionary and fill it with raw XML data.
	reports = {}
	for url in urls:
		data = fetch_source(url)

		regex_result = re.findall(r"<location name=.([^\"]*)", data)
		if len(regex_result) == 0:
			continue # Skip erroneous files with no place name.

		place_name = regex_result[0]

		# Extract the XML 'tabular' tag containing the weather forecast data.
		data = re.findall(r"<tabular[\<\>\s.\w\=\"\-\:\!\/]*</tabular>",data)[0]

		# Fill values from forecast data using keys from tags list.
		values = []
		for i in range(0, len(tags)):
			regex = tags[i][0] + r".*" + tags[i][1] + r"=\"([^\"]*)"
			values.append(re.findall(regex, data))

		reports[place_name] = values

	return reports


def print_weather_info(values):
	'''
	Takes a table of weather information in a specific format and prints the
	values to screen.

	'''

	for i in range(0, len(values[0])):
		time_from = values[0][i].replace("T", " ")
		time_to = values[1][i].replace("T", " ")
		temp = values[2][i]
		symbol = values[3][i]
		rain = values[4][i]
		wind_type = values[5][i]
		wind = values[6][i]

		print "{0} - {1}: {2}C, {3} ({4} mm), {5} ({6} m/s)".format(time_from,
					time_to, temp, symbol, rain, wind_type, wind)


def weather_update(place, hour, minute):
	'''
	Return a forecast of the given place(s) for the current time interval if
	input time is in the future, or for tomorrow's corresponding time interval
	if input time is in the past.

	'''

	reports = retrieve_weather_report(place)

	# Get current time and built a datetime-object for input time.
	current_time = datetime.now()
	given_time = "{} {}:{}:00".format(str(current_time).split()[0], str(hour), str(minute))
	timestamp = datetime.strptime(given_time, "%Y-%m-%d %H:%M:%S")

	# Add a day if given time is over for today.
	if timestamp < current_time:
		timestamp += timedelta(days = 1)
	update = str(timestamp)

	places = reports.keys()
	for place in places:
		data = reports[place]
		index = future_forecast_index(data, timestamp)

		report = [place]
		report.append(data[0][index])
		for i in range(2, 7):
			report.append(data[i][index])

		return report

def future_forecast_index(data, timestamp):
	'''
	Return index of the next forecast interval containing given timestamp.

	'''

	index = 0
	while index < len(data[0]):
		time_from = datetime.strptime(data[0][index], "%Y-%m-%dT%H:%M:%S")
		time_to = datetime.strptime(data[1][index], "%Y-%m-%dT%H:%M:%S")

		if timestamp >= time_from and timestamp <= time_to:
			break
		index += 1

	return index
