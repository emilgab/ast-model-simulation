# Classes
class Worker:
    def __init__(self, WorkerID, StartTimeAvailable, PerformanceRating, AvailabilityTime):
        self.WorkerID = str(WorkerID)
        self.StartTimeAvailable = float(StartTimeAvailable)
        self.PerformanceRating = float(PerformanceRating)
        self.AvailabilityTime = float(AvailabilityTime)
        self.AvailableToWork = True
    def __str__(self):
        return f"{self.WorkerID}: \n\tStarted working: {self.StartTimeAvailable}\
        \n\tPerformance: {self.PerformanceRating*100}%\
        \n\tRemaining availability: {self.AvailabilityTime}\
        \n\tAvailable to work at current time ({time}): {'Yes' if self.AvailableToWork else 'No'}"
    def assigned_test(self, test):
        pass

class Test:
    def __init__(self, TestID, ScheduledTime, TestTime):
        self.TestID = str(TestID)
        self.ScheduledTime = float(ScheduledTime)
        self.TestTime = float(TestTime)
    def __str__(self):
        return f"{self.TestID}: \n\tScheduled for testing at: {self.ScheduledTime}\
        \n\tTime it takes for testing: {self.TestTime}"
    def assigned_worker(self, worker):
        pass

#### PRE-FACE ####

# Start Time
start_time = 0.00

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

# Reference the workerlist file to simulate worker scenario
worker_scenario = "workerlists/1initial_increase_in_worktimes.csv"

# Reference the tasklist file to simulate test scenario
test_scenario = "tasklists/steady_flow.csv"

# NOTE:
# The following dictionaries are marked as "queues".
# These dictionaries will contain ALL tests and ALL workers in the scenario.
# The dictionaries will be checked by our simulation to know when a worker is available or when a test is submitted.
# Creates a dictionary that will later be used to store the worker objects as values where the key is the workerID
worker_dictionary_queue = {}
with open(worker_scenario,"r") as csv_file:
    for row in csv_file.readlines()[1:]:
        split_row = row.split(",")
        worker_dictionary_queue[split_row[0]] = Worker(split_row[0],split_row[1],split_row[2],split_row[3])

test_dictionary_queue = {}
with open(test_scenario,"r") as csv_file:
    for row in csv_file.readlines()[1:]:
        split_row = row.split(",")
        test_dictionary_queue[split_row[0]] = Test(split_row[0],split_row[1],split_row[2])

# Following lists will contain the active tests and workers at any given time based on the times in the tasklists and workerlists
worker_active_list = []
test_active_list = []
##################

#### SIMULATION ####

# Iterates through the times of the day
for time in times:
    # Adds the tests scheduled for current time to the "active_tests_queue" from the "test_dictionary_queue"
    tests_to_remove_from_queue = []
    for key, value in test_dictionary_queue.items():
        if str(value.ScheduledTime).ljust(5,"0") == str(time).ljust(5,"0"):
            test_active_list.append(value)
            tests_to_remove_from_queue.append(key)
    for item in tests_to_remove_from_queue:
        del test_dictionary_queue[item]
####################
