#####################################################################################
# Example program to use an Adafurit 12 LED Neopixel ring as a VLC progress indicator
# Matteo Forlani (matteo@matthew5pl.net) (c) 2022
#####################################################################################

import time, board, neopixel, vlc, sys # import needed libraries

vlc_instance = vlc.Instance("--aout=alsa") # needed for raspberry pis on buster
     
player = vlc_instance.media_player_new() # create new vlc instance
     
media = vlc_instance.media_new(sys.argv[1]) # load media file from cli args
     
player.set_media(media) # assign media file to vlc instance
     
player.play() # play one shot

pixel_pin = board.D21 # we'll use pin GPIO21 on our raspberry pi board. refer to your specific rpi model's schematics to find it.

num_pixels = 13 # number of pixels in our neopixel ring + 1

ORDER = neopixel.GRB # use correct color order for our neopixel ring

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.05, auto_write=False, pixel_order=ORDER
) # create instance of NeoPixel class

pixels.fill((0, 0, 0)) # turn all leds off
pixels.show() # calling show() is required at every led update

while True:
    total = player.get_length() # get the media's total lenght
    duration = player.get_time() # get current progress
    if duration > 0 and total > 0: # check if the media started to avoid division by 0 errors
        cur = duration/total*100 # get percentage of progress
        ledPr = cur*num_pixels/100 # multiply by the number of leds and divide by 100
        for i in range(0, int(ledPr)): # for each led
            pixels[i] = (255, 255, 255) # show current led as white
            pixels.show() # calling show() is required at every led update

# end of program
