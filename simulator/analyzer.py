from csv import reader

if __name__=="__main__":
        filename = input("What file would you like to analyze?")
        packages_on_time = 0
        packages_not_on_time = []

        
        with open(filename, 'r') as read_obj:
                csv_reader = reader(read_obj)
                lines = list(csv_reader)
                lines.pop(0)
                bruh = lines.pop()
                print(bruh, end="")
                print(" missed deadlines/undelivered packages")
                for line in lines:
                        
                        if int(line[3]) - (int(line[0]) + int(line[1])) < 0:
                                packages_on_time += 1
                        else:
                                packages_not_on_time.append(line)
                print("On Time: " + str(packages_on_time))
                print("Not On Time: " + str(len(packages_not_on_time)))
                print("Rate: " + str(float(packages_on_time)/(float(packages_on_time)+float(bruh[0])+float(len(packages_not_on_time)))))
                #print(packages_not_on_time)
        