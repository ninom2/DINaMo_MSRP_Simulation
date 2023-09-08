class Drone:
        def __init__(self, max_energy, location, capacity, model,speed=30):
                self.energy = max_energy # Current energy capacity
                self.max_energy = max_energy # Maximum energy capacity
                self.location = location # Tuple representing x and y coordinates on the city block
                self.capacity = capacity # How many packages this drone can carry
                self.model = model # Model name of drone
                self.package = None
                self.busy = False # Tells the hub whether or not the drone is currently carrying cargo
                self.speed = speed

        def __str__(self):
                return "Busy" if self.busy else "Not Busy"
        
        def rename(self, name): # NOT IN USE 
                self.model = name

        def move(self, destination): 
                # Moves drone to the specified location
                # destination must be of class Place 
                # each class has a location variable which would be used to direct the drone
                self.location = destination.location
        
        def recharge(self): # NOT IN USE
                # Recharges drone
                # NOTE: possibly add a feature here to where the drone does not fully charge up, 
                # possibly through using RL it might be found that the drone does not have to charge
                # up to full battery before being used again for maximum efficency
                self.energy = self.max_energy