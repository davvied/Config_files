#!/bin/bash
/usr/bin/emacs --daemon &

$HOME/.screenlayout/res.sh &
# nitrogen --restore &
nm-applet &
# pasystray &
/usr/lib/polkit-1/polkit-agent-helper-1 &
picom --vsync --fade-in-step=0.4 --fade-out-step=0.4 --shadow --blur-background --daemon &
