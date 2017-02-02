hue set 1 --off
hue set 2 --off --ct 500 --bri 0 --transitiontime 1
sleep 1
hue set 2 --on
sleep 1
hue set 2 --ct 300 --bri 100 --transitiontime 12000
sleep 1200
hue set 2 --ct 180 --bri 255 --transitiontime 6000
sleep 600
