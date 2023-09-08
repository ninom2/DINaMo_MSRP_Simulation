import log
import drone
import heapq
import random
import order

class Hub:
        def __init__(self, location, name, log_filename):
                self.location = location
                self.name = name
                self.packages = []
                self.index = 0
                self.drones = []
                self.package_log = log.Log(log_filename) # logs when packages were delivered, an when they were supposed to be delivered
                self.drone_info = True # toggle to turn off info about drones in console

                self.delivered_packages = {} # simply for testing purposes against duplicates
                self.duplicate_packages = 0 # also for testing against duplicates

        def __eq__(self, other):
                return 1

        def __str__(self):
                return "\U0001F50B"

        def log_undelivered_packages(self, undelivered):
                self.package_log.log_undelivered_packages(undelivered)

        def toggle_drone_info(self):
                drone_info = not drone_info

        def build_drone(self):
                new_drone = drone.Drone(0, (0,0), 0, "Basic Drone")
                self.drones.append(new_drone)

        def generate_package(self, stores, houses, current_time):
                # creates a package by picking a random store from the list of stores

                pickup_location = stores[random.randrange(0, len(stores))].location
                destination = houses[random.randrange(0, len(houses))].location
                package = order.Order(pickup_location, destination, self.location, random.randrange(4,48), 1, current_time)
                """
                print(pickup_location)
                print(destination)
                print(self.location)
                print(package.return_distance)
                print(package.delivery_distance)
                """
                heapq.heappush(self.packages,package)
                #self.packages.append(package)
                self.index += 1 # prevents TypeError

        def task_drones(self, current_time):
                """
                Searches through the hubs list of drones, checking if each drone is busy or not
                if said drone is not busy it is automaticaly given a task, if it is busy then 
                check if said drone's package is at the time in which it should be delivered
                """

                if not self.packages:
                        if not self.drones:
                                #print("No drones to be tasked")
                                #print("No packages to be taken")
                                pass
                        else:
                                for drone in self.drones: #if this loop isnt here the last drones to deliver packages will get stuck with the packages
                                        if not drone.package:
                                                drone.busy = False
                                        elif drone.package and drone.package.time_delivered == 0 and int(drone.package.delivery_distance/drone.speed + drone.package.time_placed) <= current_time:
                                                drone.package.time_delivered = current_time # the time that the drone arrived at the house
                                        elif drone.package and int((drone.package.delivery_distance + drone.package.return_distance)/drone.speed + drone.package.time_placed) <= current_time and drone.busy:
                                                self.package_log.add_entry(drone.package, current_time)
                                                drone.busy = False
                                                #print(str(drone.model) + " delivered a package")
                                                
                                                if drone.package.hash in self.delivered_packages:
                                                        self.duplicate_packages += 1

                                #print("No packages to be taken")

                else:
                        if not self.drones:
                                #print("No drones to be tasked")
                                pass
                        else:
                                for drone in self.drones:
                                        if not drone.busy:
                                                if self.packages:
                                                        drone.busy = True
                                                        drone.package = heapq.heappop(self.packages) #used for priority
                                                        #drone.package = self.packages.pop(0) # first come first served
                                                        #drone.package = self.packages.pop() # first come last served
                                                        self.index -= 1 # THIS MIGHT CAUSE ISSUES
                                                else:
                                                        pass
                                        else:
                                                # this triggers primarily
                                                if drone.package and drone.package.time_delivered == 0 and int(drone.package.delivery_distance/drone.speed + drone.package.time_placed) <= current_time:
                                                
                                                        drone.package.time_delivered = current_time # the time that the drone arrived at the house

                                                elif drone.package and int((drone.package.delivery_distance+drone.package.return_distance)/drone.speed + drone.package.time_placed) <= current_time:
                                                        self.package_log.add_entry(drone.package, current_time) # makes a log for precision checking
                                                        drone.busy = False
                                                        
                                                        if drone.package.hash in self.delivered_packages:
                                                                self.duplicate_packages += 1