# encoding: utf-8

from yr import *
import numpy as np
import datetime
import math

def build_sentence(sets, triangular=False):
    lengths = map(lambda wordset: len(wordset), sets)
    if triangular:
        random = map(lambda length: int(np.random.triangular(0, 0, length)), lengths)
    else:
        random = map(lambda length: np.random.randint(0, high=length), lengths)
    sentence = map(lambda (index, wordset): wordset[random[index]], enumerate(sets))
    return "".join(sentence)

def add_space(s):
    return s + " "

def add_comma(s):
    return s + ", "

def add_shout(s):
    return s + "! "

def add_dot(s):
    return s + ". "

def greeting():
    now = datetime.datetime.now()
    greetings = map(add_space, ["Good morning", "Rise and shine", "Wake up"])
    titles = map(add_shout, ["Sir", "Master", "Hero", "Commander", "Handsome", "Great leader", "Comrade"])
    extras = map(add_space, ["I hope you slept well.", "How are you today?", "I honestly thought you were dead."])

    if int(now.minute) is 0:
        time = ["The time is {} o clock. ".format(now.hour)]
    else:
        time = ["The time is {} minutes past {}. ".format(now.minute, now.hour)]

    return build_sentence([greetings, titles, extras, time], triangular=True)

def forecast(report):
    temp = report[2]
    weather_type = report[3]
    rain_amount = report[4]
    wind_type = report[5]
    wind_speed = report[6]

    message = ""

    if temp < 0:
        message += "You better turn the heat up, because the temperature is expected to reach {} degrees. ".format(temp)
    else:
        message += "Todays forecast for Oslo is {} degrees. ".format(temp)

    if "rain" in weather_type.lower() or "snow" in weather_type.lower():
	if rain_amount > 4:
		message += "Best bring your umbrella today. "
        message += "Expect around {} mm of {}. ".format(rain_amount, weather_type)
    else:
	message += "Expect a {} weather type today. ".format(weather_type)

    message += "The weather is accompanied with a {} of {} m/s. " .format(wind_type, wind_speed)
    return message

def news():
    message = "Here's your favorite radio channel."
    return message

def wake():
    message = greeting()

    morning = weather_update("Oslo", 9, 00)
    message += forecast(morning)
    message += news()

    return message

print "\"" + wake() + "\""
