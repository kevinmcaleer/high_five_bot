# test_calibrate

from stepper_28byj48 import BYJ28
from time import sleep

stepper  = BYJ28([10,11,12,13])
steps = 130
direction = False
delay = 0.001

def calibrate_position():
    direction = True
    
    while True:
        print("""
            Press a for +10 steps
            Press d for -10 steps
            Press z for +1 step
            Press c for - 1 step
            Press w to change direction
            press q to quit
        """)
        command = input(">")
        if command in ['a','d','q','z','c']:
            if command == 'a':
                stepper.move_motor(1,direction)
            if command == 'w':
                direction = not direction
            if command == 'z':
                stepper.move_motor(1,direction)
            if command == 'c':
                stepper.move_motor(1,not direction)
            if command == 'd':
                stepper.move_motor(10, (not direction))
            if command == 'q':
                return 

def calibrate_90():
    direction = True 
    stepper.move_motor(steps, not direction)
    sleep(1)
    stepper.move_motor(steps,  direction)

def default_position():
    stepper.move_motor(steps, not direction, delay)
    sleep(0.1)

# Un-comment the lines below to use the calibrate position, calibrate 90 degree
# or to move the hand to the default position

# calibrate_position()
# calibrate_90()
default_position()

    
    