#!/bin/bash
echo "Pierra said:" $1
echo $1 > input
read buffer < input

# Compile and say input message.
sudo pico2wave -w=speech.wav "${buffer}" >& trash
sudo aplay speech.wav >& trash

rm input
rm trash
