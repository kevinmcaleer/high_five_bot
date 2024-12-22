# test_calibrate

from stepper_28byj48 import BYJ28

motor  = BYJ28([10,11,12,13])
direction = True

while True:
    print("""
        Press a for +10 steps
        Press d for -10 steps
        Press w to change direction
        press q to quit
""")
    command = input(">")
    if command in ['a','d','q']:
        if command == 'a':
            motor.move_motor(10,direction)
        if command == 'w':
            direction = not direction
        if command == 'd':
            motor.move_motor(10, (not direction))
        if command == 'q':
            break 
    