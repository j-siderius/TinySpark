# Import all libraries
import board
import neopixel

# Define the Neopixel pin
pixel_pin = board.NEOPIXEL

# Initialize the Neopixel object
num_pixels = 5
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False, pixel_order=neopixel.GRB)

# Fill all pixels with BLACK and then show
pixels.fill((0, 0, 0))
pixels.show()