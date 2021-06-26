#!/bin/bash

# see man zscroll for documentation of the following parameters
zscroll -l 25 \
        --delay 0.3 \
        --scroll-padding " ⏽ " \
        --match-command "playerctl --player=spotify,firefox status" \
        --match-text "Playing" "--scroll 1" \
        --match-text "Paused" "--scroll 0" \
        --match-text "Playing" "--before-text '  ' --scroll 1" \
        --match-text "Paused" "--before-text '  ' --scroll 0" \
        --update-check true "playerctl --player=spotify,firefox metadata --format \"{{ title }} - {{ artist }}\"" &


wait
