from stepper_28byj48 import BYJ28

stepper = BYJ28([10,11,12,13])


stepper.move_motor(512, 1,0.001)
