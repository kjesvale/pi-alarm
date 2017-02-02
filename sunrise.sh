hue set 1 --off
hue set 2 --off --ct 500 --bri 0 --transitiontime 1
sleep 1
hue set 2 --on
sleep 1
hue set 2 --ct 300 --bri 100 --transitiontime 200
sleep 20
hue set 2 --ct 180 --bri 255 --transitiontime 100
