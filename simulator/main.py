import hub
import house
import store
import random
import heapq

def print_grid(grid):
        for i in range(0, len(grid)):
                for j in range(0,len(grid)):
                        print(str(grid[i][j]) + ", ", end="")
                print("\n")




if __name__=="__main__":

        city_width, city_height = (100, 100)
        grid = []
        for i in range(0, city_width):
                grid.append([0]*city_height)

        
        simulation = True
        city_exists = False
        display_grid = False
        time_of_day = 0 # used for calculating time
        choice = 9999 # Used for user input
        rand_seed = 0 # Seed for random generation throughout the simulation
        hub_coords = [0,0] # set later on
        houses = [] # list of all houses
        stores = []
        
        while simulation:
                if display_grid: print_grid(grid)
                print("Select a number to choose of what to do")
                print("1. Populate Cityscape with Stores, Houses and a Drone Hub (This will erase the current cityscape)")                
                print("2. Place order")
                print("3. Next Hour")
                print("4. Run for Set Amount of Time")
                print("5. Toggle Display")
                print("6. Build Drones")

                print("7. Exit")

                while choice < 1 or choice > 8:
                        choice = int(input())

                if choice == 1:
                        rand_seed = input("Select any integer seed(MUST BE A NUMBER):")
                        rand_seed = int(rand_seed)
                        random.seed(rand_seed)
                        
                        log_filename = str(input("Select a file name, INCLUDE file extension, DO NOT use a filename that has been used before, or enter 'no' to not save to a file'"))

                        # loop fills up the matrix with House and Store objects, theres a 40% chance that a house will spawn and a 20% chance that a store will spawn
                        for i in range(0, city_width):
                                for j in range(0, city_height):
                                        rand_num = random.randrange(0,10)
                                        if rand_num < 4:
                                                home = house.House((i,j))
                                                grid[i][j] = home
                                                houses.append(home)
                                        elif rand_num > 7:
                                                shop = store.Store((i,j), "Generic Store")
                                                grid[i][j] = shop
                                                stores.append(shop)
                                        else:
                                                grid[i][j] = 0

                        #place hub
                        hub_coords = [random.randrange(0,5), random.randrange(0,5)]
                        main_hub = hub.Hub(hub_coords, "HeadQuarters", log_filename)                        
                        #random.shuffle(houses)
                        #random.shuffle(stores)
                        grid[hub_coords[0]][hub_coords[1]] = main_hub
                        city_exists = True
                if choice == 2:
                        if city_exists:
                                main_hub.generate_package(stores, houses, time_of_day)
                        else:
                                print("Populate Grid First")

                if choice == 5:
                        display_grid = not display_grid
                if choice == 4:
                        num_steps = int(input("How many time steps shall the simulation run for?"))
                        num_packages_per_step = int(input("How many packages shall be generated at each time step?"))
                        for i in range(0, num_steps):
                                for j in range(0, num_packages_per_step):
                                        main_hub.generate_package(stores, houses, time_of_day)
                                main_hub.task_drones(time_of_day)
                                time_of_day += 1
                        
                if choice == 3:
                        main_hub.task_drones(time_of_day)
                        time_of_day += 1
                        
                if choice == 6:
                        if city_exists:
                                num_drones = int(input("How many drones would you like to build?"))
                                for i in range(0, num_drones):
                                        main_hub.build_drone()
                        else:
                                print("Generate a city with a hub before building drones")
                if choice == 7:
                        if city_exists:
                                print(str(main_hub.duplicate_packages) + " duplicate packages")
                        
                        undelivered = 0
                        for package in main_hub.packages:
                                if package.deadline <= time_of_day:
                                        undelivered += 1
                        main_hub.log_undelivered_packages(undelivered)

                        simulation = False
                if choice == 8: # hidden testing feature
                        for package in main_hub.packages:
                                print(heapq.heappop(main_hub.packages))
                choice = 9999

                