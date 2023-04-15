#!/usr/bin/env python3

regular_colors = [
    "\033[0;30m",
    "\033[0;31m",
    "\033[0;32m",
    "\033[0;33m",
    "\033[0;34m",
    "\033[0;35m",
    "\033[0;36m",
    "\033[0;37m",
]

bold_colors = [
    "\033[1;30m",
    "\033[1;31m",
    "\033[1;32m",
    "\033[1;33m",
    "\033[1;34m",
    "\033[1;35m",
    "\033[1;36m",
    "\033[1;37m",
]

color_names = [
    "Black",
    "Red",
    "Green",
    "Yellow",
    "Blue",
    "Magenta",
    "Cyan",
    "White",
]


for i, (v1, v2) in enumerate(zip(regular_colors, bold_colors)):
    print("\033[0m" + color_names[i].ljust(10) + " " * 5 + v1 + "█" * 5 + " " + v2 + "█" * 5)
