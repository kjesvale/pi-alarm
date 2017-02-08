minutes=${1:-30}
deciseconds=$((minutes * 600))
twothirds=$((deciseconds * 2/3))
onethird=$((deciseconds / 3))

hue set 1 --off --ct 500 --bri 0 --transitiontime 1
hue set 2 --off --ct 500 --bri 0 --transitiontime 1

sleep 1

hue set 1 --on
hue set 2 --on

sleep 1

hue set 1 --ct 380 --bri 10 --transitiontime "$twothirds"
hue set 2 --ct 380 --bri 100 --transitiontime "$twothirds"

sleep $(($twothirds / 10))

hue set 1 --ct 217 --bri 50 --transitiontime "$onethird"
hue set 2 --ct 217 --bri 255 --transitiontime "$onethird"

sleep $(($onethird / 10))
hue stop
