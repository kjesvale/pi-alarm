import requests
import json
import time

user_config = open('hue.config', 'r')
hue_ip = user_config.readline().strip()
user_id = user_config.readline().strip()

base_url = 'http://' + hue_ip + '/api/' + user_id + '/'
light_1 = base_url + 'lights/1/state'
light_2 = base_url + 'lights/2/state'
group = base_url + 'groups/1/action'

delay = 1

# Turn the lights on
#requests.put(group_state, data = json.dumps({ 'on': True, 'bri': 254, 'sat': 254 }))
print 'Turned the lights on.'

bri = 1

#r = requests.get(base_url + 'lights/1/')
r = requests.put(light_1, data = json.dumps({ 'on': True, 'bri': bri, 'ct': 286 }))

print r.json()

#while True:
#    hue = 1
#
#    while (hue < 65000):
#        r1 = requests.put(group_state, data = json.dumps({ 'hue': hue }))

#        time.sleep(delay)
#        print(r1.json())
#        hue += 1000
