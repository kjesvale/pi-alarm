import time
import os
import subprocess
import sys

alarms = []

def read_config():
	global alarms
	alarms = []
	file = open('alarm.config', 'r')
	for line in file:
		items = line.split(':')
		alarms.append({'hour': int(items[0]), 'min': int(items[1])})

	file.close()

def print_alarms():
	if len(alarms) == 0:
		print '  There is currently no alarms configured. Exiting ...'
		sys.exit()
	else:
		print '  Scheduled alarms:'
		for index, alarm in enumerate(alarms):
			print '  {}: {}:{}'.format(index + 1, alarm['hour'], alarm['min'])
		print ''

def run():
	now = time.localtime()
	for alarm in alarms:
		if now.tm_hour == alarm['hour'] and now.tm_min == alarm['min']:
			subprocess.call('./wakeup_sequence.sh', shell = True)
	
	time.sleep(60)
	read_config()

print 'Initializing alarm clock.'
print '  Time is currently {}\n'.format(time.ctime())

read_config()
while True:
	run()
