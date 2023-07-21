#!/bin/bash
dbus-monitor --session "type='signal',interface='org.gnome.ScreenSaver'" | \
( while true
    do read X
    if echo $X | grep "boolean true" &> /dev/null; then
        echo "locking at $(date)" >> /home/adarsh/time_xprofile
    elif echo $X | grep "boolean false" &> /dev/null; then
        python3 /home/adarsh/welcome.py 
    fi
    done )
