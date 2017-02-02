import requests
import json
import time

user_config = open('hue.config', 'r')
hue_ip = user_config.readline().strip()
user_id = user_config.readline().strip()

base_url = 'http://' + hue_ip + '/api/' + user_id + '/'
group = base_url + 'groups/1/action'

wakeup_duration = 30
light_max_value = 254
sleep_duration = (wakeup_duration * 60) / 254

# Initial light settings to ensure they're on and has the correct color temp.
requests.put(group, data = json.dumps({ 'on': True, 'bri': 0, 'ct': 286 }))

print 'Wakeup sequence initialized.'

bri = 0
while bri < 255:
	result = requests.put(group, data = json.dumps({ 'bri': bri, }))
	print "{}: {}".format(bri, result.json())
	time.sleep(sleep_duration)
	bri += 1

print 'Wakeup sequence completed.'
