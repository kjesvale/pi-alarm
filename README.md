# pi-alarm

A Raspberry PI alarm clock that tells you the weather when you wake up.

### Features:

* Creates a sunrise effect using Philips hue (30 minutes)
* Tells you the weather, fetched from yr.no
* Plays a recently recorded news clip from an internet radio

### How it works

* I manage a *crontab* file where I schedule various tasks for the computer to run.
* At 06:30 (07:00 on weekends), I run the *record_radio* script which records the next *n* minutes of the radio station specified in *radio.config*.
* My config points to the Norwegian radio station NRK P3, which sends a news summary of three minutes at said times.
* Some time before I want the alarm to run, I schedule the *wakeup_sequence* script.
* The wakeup script will slowly lighten my Philips Hue bulbs, transitioning from a warm sunrise (~3200K) to a colder daylight (~6500K).
* At full brightness, the alarm will fire, telling me the weather and playing the recorded news clip.

