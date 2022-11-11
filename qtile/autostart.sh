#!/bin/bash
### UNCOMMENT ONLY ONE OF THE FOLLOWING THREE OPTIONS! ###
# 1. Uncomment to restore last saved wallpaper
# xargs xwallpaper --stretch < ~/.cache/wall &
# 2. Uncomment to set a random wallpaper on login
# find /usr/share/backgrounds/elementary_wallpapers -type f | shuf -n 1 | xargs xwallpaper --stretch &
find /home/mpc-man/Pictures/wallpaper -type f | shuf -n 1 | xargs xwallpaper --stretch &
# 3. Uncomment to set wallpaper with nitrogen
