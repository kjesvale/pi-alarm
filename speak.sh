#!/bin/bash
echo "Pierra said:" $1
echo $1 > input
read buffer < input

# Compile and say input message.
pico2wave -w=speech.wav "${buffer}"
#aplay speech.wav &> /dev/null
sox -v 0.9 speech.wav -r 48k speech.mp3 gain -6 treble +6 &> /dev/null
mplayer speech.mp3 &> /dev/null

rm input
