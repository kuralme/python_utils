#!/usr/bin/env python
"""
Test X11 display device and get the name
"""

from Xlib import X, display

# Create a connection to the X11 display
d = display.Display()

# Get the name of the display
display_name = d.get_display_name()

# Get the default screen and root window
screen = d.screen()
root = screen.root

# Create a new window
win = root.create_window(
    100, 100, 400, 300,  # x, y, width, height
    1,                   # border width
    screen.root_depth,
    background_pixel=screen.white_pixel
)

# Map the window to the display and display it
win.map()
d.flush()

# Print the name of the display
print("Display name: {}".format(display_name))

# Enter the main event loop
while True:
    event = d.next_event()
    # Handle X11 events here


