# encoding: utf-8

import datetime
import os.path, re, sys

class Lazy:
	def __init__(self, func, timestamp = ""):
		self.func = func
		self.timestamp = timestamp

	def __call__(self, arg):
		'''
		Stores the buffered results in a file so they persist
		after reopening the program.

		'''

		return self.retrieve(arg)

	def retrieve(self, arg):
		'''
		Check if there exists a file with name 'arg'. If so, return the content
		of said file. If not, run func(arg), store the result in a new file
		and return it.

		'''

		filepath = "cache/" + arg.replace("/", "_")

		try:
			# Throws an IOError if the file does not exist.
			test_if_exists = open(filepath)
			test_if_exists.close()

			arg_file = open(filepath, 'r')
			value = arg_file.read()

			if "forecast.xml" in arg:
				if self.outdatedXML(value):
					value = self.store(arg, filepath)
			elif self.outdated(value, filepath):
				value = self.store(arg, filepath)

			arg_file.close()

		except IOError as e:
			# Could not find any file with name 'arg'
			value = self.store(arg, filepath)

		return value

	def store(self, arg, filepath):
		value = self.func(arg)
		arg_file = open(filepath, 'w')
		arg_file.write(value)
		arg_file.close()
		return value


	def outdatedXML(self, data):
		'''
		Check the <nextupdated> tag on the cached file and return true if the
		current time (now) has passed said timestamp.

		'''

		pattern = r"<nextupdate>([^<]*)"
		regex_result = re.findall(pattern, data, re.IGNORECASE)
		if len(regex_result) == 0:
			return 1 # XML file has an error, try to update it.

		next_update = regex_result[0]
		next_update = datetime.datetime.strptime(next_update, "%Y-%m-%dT%H:%M:%S")

		return self.getCurrentTime() > next_update

	def outdated(self, data, filepath):
		'''
		Look at the file's "last modified" timestamp and return whether file
		is more than six hours old.

		'''

		epoch = os.path.getmtime(filepath)
		last_modified = datetime.datetime.fromtimestamp(epoch)
		six_hours = datetime.timedelta(0, 21600)

		return self.getCurrentTime() > last_modified + six_hours

	def getCurrentTime(self):
		now = self.timestamp
		if now is "":
			now = datetime.datetime.now()
		else:
			try:
				now = datetime.datetime.strptime(now, "%Y-%m-%d %H:%M:%S")
			except ValueError as e:
				print "Error: wrong format for optional timestamp \"" + now + \
					  "\", uses current time instead."
				now = datetime.datetime.now()

		return now
