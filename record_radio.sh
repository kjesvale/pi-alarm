cd /home/pi/alarm/recordings

# Duration of recording
duration=${1:-3}
seconds=$(($duration * 60))

# Radio station stream to record from
radio_station=`sed -n '1p' ../radio.config`

file_name=dagsnytt${duration}

# Remove old files
rm ${file_name}.mp3
rm ${file_name}.cue

# Store the recording in /recordings
arguments="${radio_station} -l ${seconds} -A -s -a ${file_name}.mp3 --quiet"
streamripper ${arguments}
