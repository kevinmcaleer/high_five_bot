from time import sleep
from range_finder import RangeFinder

distance = RangeFinder(trigger_pin=1, echo_pin=0)

while True:
    
    print(f" Distance = {distance.distance}")
    
    sleep(1)