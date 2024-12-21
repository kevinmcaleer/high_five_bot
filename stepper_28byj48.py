from machine import Pin
from time import sleep

class BYJ28:
    """
    Minimal driver example for a 28BYJ-48 stepper motor
    using 4 control pins on a MicroPython board.
    """

    # Default pins used here: GPIO11, GPIO12, GPIO13, GPIO15
    # Adjust as needed for your board.
    def __init__(self, pins=[11, 12, 13, 15]):
        # Create and store Pin objects for each pin in OUTPUT mode
        self.pins = [Pin(pin_num, Pin.OUT) for pin_num in pins]

        # Full-step sequence for 28BYJ-48
        self.step_sequence = [
            [1, 0, 0, 1],
            [1, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 1],
            [0, 0, 0, 1],
        ]
        print("Stepper Motor init complete")

    def move_motor(self, steps, direction=1, delay=0.002):
        """
        Rotate the motor a given number of steps.
        
        :param steps: Number of steps to rotate (int)
        :param direction: 1 for forward, -1 for reverse
        :param delay: Delay between steps in seconds
        """
        # Decide which sequence to use based on direction
        if direction == 1:
            sequence = self.step_sequence
        else:
            # Reverse the sequence for the opposite direction
            sequence = list(reversed(self.step_sequence))

        print("Moving Motor")
        # Perform the requested number of steps
        for _ in range(steps):
            # For each set of outputs in the step sequence
            for step_values in sequence:
                # Write each bit in step_values to the corresponding pin
                for pin, value in zip(self.pins, step_values):
                    pin.value(value)
                sleep(delay)
