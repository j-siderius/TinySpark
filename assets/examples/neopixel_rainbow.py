# Import all libraries
import time
import math
import board
import neopixel

# Define the Neopixel pin
pixel_pin = board.NEOPIXEL

# Initialize the Neopixel object
num_pixels = 5
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False, pixel_order=neopixel.GRB)

def rainbow(wait):
    # Cycle through all hue values
    for i in range(255):
        # Calculate the R, G, B values using sines
        hue = i / 255
        r = round(255 * (abs(math.sin(hue * 2 * math.pi))))
        g = round(255 * (abs(math.sin((hue + 1 / 3) * 2 * math.pi))))
        b = round(255 * (abs(math.sin((hue + 2 / 3) * 2 * math.pi))))
        
        # Fill all pixels in the chosen colour
        pixels.fill((r, g, b))
        # Show / Update the pixels
        pixels.show()
        time.sleep(wait)

# Call the rainbow function and change colours every 20ms
while True:    
    rainbow(0.02)