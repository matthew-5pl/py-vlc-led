# py-vlc-led
Small python program to show a song's process using an led ring
# Usage 
This program is to be used with a Raspberry Pi.<br>
Depending on the GPIO pin you want to use and the amount of LEDs in your ring, you might need to edit some variables in the program,
specifically `pixel_pin` and `num_pixels`.<br>
The wiring is as such in the default configuration:
| Neopixel Ring | Raspberry Pi |
|---------------|--------------|
| 5V DC         | 5V           |
| GND           | GND          |
| Data Input    | GPIO21       |


Then run the script specifying a path to an audio file as a cli argument.
