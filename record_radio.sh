cd /home/pi/alarm/recordings

duration=${1:-3}
seconds=$(($duration * 60))
radio_station=`sed -n '1p' ../radio.config`
file_name=dagsnytt${duration}

arguments="${radio_station} -l ${seconds} -A -s -a ${file_name}_tmp.mp3 --quiet"
streamripper ${arguments}

# Replace old recordings
rm ${file_name}.mp3
rm ${file_name}.cue
mv ${file_name}_tmp.mp3 ${file_name}.mp3
mv ${file_name}_tmp.cue ${file_name}.cue
