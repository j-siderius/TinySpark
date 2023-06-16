 # Include the nescessary pins
import microcontroller
import board

# Start an empty array for storing the found pins
board_pins = []

# Loop through all pins in the microcontroller directory
for pin in dir(microcontroller.pin):

    # Check if a pin has been seen before
    if isinstance(getattr(microcontroller.pin, pin), microcontroller.Pin):
        pins = []
        
        # Add the pin to aliasses if found before
        for alias in dir(board):
            if getattr(board, alias) is getattr(microcontroller.pin, pin):
                pins.append("board.{}".format(alias))
        if len(pins) > 0:
            board_pins.append(" ".join(pins))

# Print all pins
for pins in sorted(board_pins):
    print(pins)