#!/bin/bash
echo "Pierra said:" $1
echo $1 > input
read buffer < input
sudo pico2wave -w=speech.wav "${buffer}" >& trash
sudo aplay speech.wav >& trash
rm input
#sudo rm speech.wav
sudo timeout 60s mplayer http://lyd.nrk.no/nrk_radio_p3_mp3_h >& trash
rm trash
