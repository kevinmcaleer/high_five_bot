from stepper_28byj48 import BYJ28
from time import sleep

stepper = BYJ28([0,1,2,3]) # Pass an list of 4 GPIO Pin numbers

steps = 5    # 130 is 90 degrees
direction = False # False is clockwise, True is anti-clockwise
delay = 0.001

stepper.move_motor(steps, direction ,delay)

#stepper.move_motor(steps, not direction, delay)
