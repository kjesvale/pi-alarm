# Read settings from config file.
radio_station=`sed -n '1p' radio.config`
duration=`sed -n '2p' radio.config`

# Play station for the given duration
timeout ${duration}s mplayer ${radio_station} </dev/null >/dev/null 2>&1 &

