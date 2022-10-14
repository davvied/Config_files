#!/usr/bin/env bash

/usr/bin/emacs --daemon &

/home/lin/.screenlayout/res.sh &
### UNCOMMENT ONLY ONE OF THE FOLLOWING THREE OPTIONS! ###
# 1. Uncomment to restore last saved wallpaper
# xargs xwallpaper --stretch < ~/.cache/wall &
# 2. Uncomment to set a random wallpaper on login
find /usr/share/backgrounds/elementary_wallpapers -type f | shuf -n 1 | xargs xwallpaper --stretch &
# 3. Uncomment to set wallpaper with nitrogen
# nitrogen --restore &
nm-applet &
picom --no-vsync --fade-in-step=0.4 --fade-out-step=0.4 --shadow --blur-background --daemon
