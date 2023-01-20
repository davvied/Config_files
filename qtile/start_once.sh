#!/bin/fish
/usr/bin/emacs --daemon &
eval (ssh-agent -c) &
$HOME/.screenlayout/res.sh &
# nitrogen --restore &
nm-applet &
firewall-applet &
# pasystray &
polkit-dumb-agent &
picom --vsync --fade-in-step=0.4 --fade-out-step=0.4 --shadow --blur-background &
