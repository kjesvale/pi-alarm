#!/bin/bash
python build_message.py | xargs ./speak.sh
./play_radio.sh