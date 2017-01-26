# Read settings from config file.
radio_station=`sed -n '1p' radio.config`
duration=`sed -n '2p' radio.config`

# Play station for 
sudo timeout ${duration}s mplayer ${radio_station} >& trash
rm trash