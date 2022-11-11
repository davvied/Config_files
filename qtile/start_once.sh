#!/bin/bash
#!/usr/bin/env bash

/usr/bin/emacs --daemon &

# /home/lin/.screenlayout/res.sh &
# nitrogen --restore &
# nm-applet &
picom --vsyn --fade-in-step=0.4 --fade-out-step=0.4 --shadow --blur-background --daemon &
