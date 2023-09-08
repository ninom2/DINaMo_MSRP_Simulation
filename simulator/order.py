import math
import random

def dist(a, b):
        return int(math.sqrt(pow((a[1] - b[1]), 2) + pow((a[0] - b[0]), 2)))

class Order:
        def __init__(self, origin, destination, hub_location, deadline, weight, time_placed):
                self.origin = origin #MUST BE A TUPLE
                self.weight = weight
                self.destination = destination #MUST BE A TUPLE
                self.delivery_distance = dist(hub_location, origin) + dist(origin, destination)
                self.return_distance = dist(destination, hub_location)
                self.deadline = deadline #+ int((self.delivery_distance+self.return_distance)/3)
                self.time_placed = time_placed
                self.time_delivered = 0
                self.hash = random.getrandbits(128) # this is to test if the same packages has been added to the log twice, which would cause the data to be inaccurate

        def __str__(self):
                return str(self.delivery_distance + self.return_distance)

        def __lt__(self, other):
                return (self.delivery_distance+self.return_distance) < (other.delivery_distance+other.return_distance)
                #return (self.delivery_distance) < (other.delivery_distance)
                #return (self.deadline) < (other.deadline)
