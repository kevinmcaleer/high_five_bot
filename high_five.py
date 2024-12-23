# Import stepper motor driver - BYJ28
# import range finder code

from range_finder import RangeFinder
from stepper_28byj48 import BYJ28
from time import sleep

# Create a RangeFinder object
range_finder = RangeFinder(trigger_pin=1, echo_pin=0)
stepper = BYJ28([10,11,12,13])

direction = False
hit_range = 20

steps = 130
delay = 0.001

def high_five():
    stepper.move_motor(steps, direction, delay)
    sleep(0.1)

def default_position():
    stepper.move_motor(steps, not direction, delay)
    sleep(0.1)

was_in_high_five = False  # Flag to track the current position state

while True:
    distance = range_finder.distance
    print(f"Distance: {distance}")

    if distance < hit_range:
        # If the arm is not already in high five position, do high five
        if not was_in_high_five:
            high_five()
            was_in_high_five = True      
    else:
        # Only return to default position if the arm was previously in high five
        if was_in_high_five:
            default_position()
            was_in_high_five = False
    sleep(1)
        
