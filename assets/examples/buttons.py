# Include all libraries
import time
import board
from digitalio import DigitalInOut, Direction, Pull

# Initialise button 1, declare it as input and pull it up in software
button1 = DigitalInOut(board.BUTTON1)
button1.direction = Direction.INPUT
button1.pull = Pull.UP

# Initialise button 2, declare it as input and pull it up in software
button2 = DigitalInOut(board.BUTTON2)
button2.direction = Direction.INPUT
button2.pull = Pull.UP

# Check if buttons are pressed (buttons are pulled HIGH, so check for low)
while True:
    if not button1.value:
        print("Button 1 pressed!")
    if not button2.value:
        print("Button 2 pressed!")
    
    # Small delay to avoid spamming
    time.sleep(0.1)