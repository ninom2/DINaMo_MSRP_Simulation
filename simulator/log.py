class Log:
        def __init__(self, filename):
                self.filename = filename
                if filename.lower() == "no": 
                        self.save = False
                else:
                        self.save = True
                        self.filename = "testdata/" + filename
                if self.save: 
                        f = open(self.filename, "x")
                        f.write("Time Placed, Deadline, Drone Return Time, Time Delivered, Delivery Distance, Return Distance\n")
                        f.close()
        def add_entry(self, package, return_time):
                if self.save:
                        f = open(self.filename, "a")
                        f.write(str(package.time_placed) + "," + str(package.deadline) + "," + str(return_time) + "," + str(package.time_delivered) + "," + str(package.delivery_distance) + "," + str(package.return_distance) + "\n")
                        f.close()
        
        def log_undelivered_packages(self, undelivered):
                if self.save:
                        f = open(self.filename, "a")
                        f.write(str(undelivered))
                        f.close()