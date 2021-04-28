import random
import csv
import string

# Creating the dictionaries that will consist of our workers
worker_initial_dictionary = {}
worker_additional_dictionary = {}

# Worker counter used for creating worker ID's
worker_increment = 1

# Variable that consists of the number of workers that the taskfile should start of with
initial_workers = 4

# iterates over the range of the integer set in the initial_workers and uses enumerate
for _ in range(0,initial_workers):
    # Creates an entry in the dictionary that consists of the WorkID as key: "W0001" and values for StartTimeAvailable, PerformanceRating and AvailabilityTime
    worker_initial_dictionary["W"+str(worker_increment).zfill(4)] = {
                                                    "StartTimeAvailable":'0.00',
                                                    "PerformanceRating":round(random.uniform(0.6,2),2),
                                                    "AvailabilityTime":round(random.uniform(20,180),2),
                                                    }
    # incrementing with 1
    worker_increment += 1

# Uses list comprehension to create the 24 hours (0-23).
hrs = [str(x) for x in range(0,24)]
# Uses list comprehension to create the minutes in an hour (0-59)
# Uses .zfill() to create (00, 01, 02, 03 instead of 0,1,2,3)
min = [str(x).zfill(2) for x in range (0,60)]
# list called "times" that will consist of all the times through a day: "00.00-23.59".
times = []
# for-loop that iterates through the hrs and min lists and creates the times for a day.
for x in hrs:
    for y in min:
        times.append(f"{x}.{y}")

# Iterates through each time of the day
for time in times:
    # This try/except block will introduce an increase in workers at the hours 10:00-18:59
    # try:
    #     new_time = int(time[0:2])
    #     if new_time in range(10,18):
    #         for additionals in range(1,6):
    #             chance = random.randint(0,8)
    #             if chance == 1:
    #                 worker_additional_dictionary["W"+str(worker_increment).zfill(4)] = {
    #                     "StartTimeAvailable": time,
    #                     "PerformanceRating":round(random.uniform(0.6,2),2),
    #                     "AvailabilityTime":round(random.uniform(20,180),2),
    #                 }
    #                 worker_increment += 1
    # except:
    #     pass
    # This for-loop add additional workers (additional as in addition to the initial workers) to the dictionary called "worker_additional_dictionary"
    for additionals in range(1,4):
        chance = random.randint(0,34)
        if chance == 1 or chance == 6:
            worker_additional_dictionary["W"+str(worker_increment).zfill(4)] = {
                "StartTimeAvailable": time,
                "PerformanceRating":round(random.uniform(0.6,2),2),
                "AvailabilityTime":round(random.uniform(20,180),2),
            }
            worker_increment += 1

# Combines the two dictoinaries
total_workers_dictionary = {**worker_initial_dictionary, **worker_additional_dictionary}

# Defines the filename for the CSV file
csv_filename = "WORKERFILENAME.csv"
# CSV FILE
with open(csv_filename,"w") as csv_file:
    worker_writer = csv.writer(csv_file, quotechar='"', quoting=csv.QUOTE_MINIMAL)
    worker_writer.writerow(["WorkerID","StartTimeAvailable","PerformanceRating","AvailabilityTime"])
    for x,y in total_workers_dictionary.items():
        worker_writer.writerow([x,y["StartTimeAvailable"],y["PerformanceRating"],y["AvailabilityTime"]])

######## FOR GRAPH ############
counter_dict = {}

for time in times:
    for x,y in total_workers_dictionary.items():
        if float(time) == float(y["StartTimeAvailable"]):
            if float(time) in counter_dict:
                counter_dict[float(time)] += 1
            else:
                counter_dict[float(time)] = 1
        else:
            counter_dict[time] = 0


plot_graph = [[]]
for x,y in counter_dict.items():
    plot_graph[0].append((x,y))

# print(plot_graph)
