# Classes
class Worker:
    instances = []
    def __init__(self, WorkerID, StartTimeAvailable, PerformanceRating, AvailabilityTime):
        self.WorkerID = str(WorkerID)
        self.StartTimeAvailable = float(StartTimeAvailable)
        self.PerformanceRating = float(PerformanceRating)
        self.AvailabilityTime = float(AvailabilityTime)
        self.AvailableToWork = True
        self.AssignedTests = []
        self.CompletedTests = []


        self.instances.append(self)
    def __str__(self):
        return f"{self.WorkerID}: \n\tStarted working: {self.StartTimeAvailable}\
        \n\tPerformance: {self.PerformanceRating*100}%\
        \n\tRemaining availability: {self.AvailabilityTime}\
        \n\tAvailable to work at current time ({time}): {'Yes' if self.AvailableToWork else 'No'}\
        \n\tAssignedTests: {' '.join(self.AssignedTests)}"
    def assigned_test(self, test):
        self.AvailableToWork = False
        self.AssignedTests.append(test)

class Test:
    instances = []
    def __init__(self, TestID, ScheduledTime, TestTime):
        self.TestID = str(TestID)
        self.ScheduledTime = float(ScheduledTime)
        self.TestTime = float(TestTime)
        self.AssignedWorker = "N/A"

        self.instances.append(self)
    def __str__(self):
        return f"{self.TestID}: \n\tScheduled for testing at: {self.ScheduledTime}\
        \n\tTime it takes for testing: {self.TestTime}\
        \n\tAssigned to worker: {self.AssignedWorker}"

    def assigned_worker(self, worker):
        self.AssignedWorker = worker

### PRE-PHASE ###

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
worker_scenario = "workerlists/1initial_increase_in_worktimes_sample.csv"

# Reference the tasklist file to simulate test scenario
test_scenario = "tasklists/steady_flow_sample.csv"

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
active_worker_list = []
active_test_list = []

# This dictionary will contain information regarding the completed tests.
completed_test_dictionary = {}

### END OF PRE-PHASE ###

### SIMULATION ###
### |
# Iterates through the times of the day
for time in times:
    ### --> SIMULATION "CHECK"-PHASE: Checking the queue dictionaries and adding them in the active lists <-- ###
    # Adds the tests scheduled for current time to the "active_tests_queue" from the "test_dictionary_queue"
    tests_to_remove_from_queue = []
    for key, value in test_dictionary_queue.items():
        if str(value.ScheduledTime).ljust(5,"0") == str(time).ljust(5,"0"):
            active_test_list.append(value)
            tests_to_remove_from_queue.append(key)
    for item in tests_to_remove_from_queue:
        del test_dictionary_queue[item]
    # Adds the available workers to active workers list from the worker_dictionary_queue.
    workers_to_remove_from_queue = []
    for key, value in worker_dictionary_queue.items():
        if str(value.StartTimeAvailable).ljust(5,"0") == str(time).ljust(5,"0"):
            active_worker_list.append(value)
            workers_to_remove_from_queue.append(key)
    for item in workers_to_remove_from_queue:
        del worker_dictionary_queue[item]
    ### END "CHECK"-PHASE ###
    ### |
    ### |
    ### |
    ### --> SIMULATION "CHECK FOR AVAILABLE WORKERS PHASE": Checks for workers that are finished working and are now available <-- ###
    for key, value in worker_dictionary_queue.items():
        if str(value.AvailableToWork) == True and value not in worker_active_list:
            active_worker_list.append(value)
    ### END "CHECK FOR AVAILABLE WORKERS PHASE" ###
    ### |
    ### |
    ### |
    ### --> SIMULATION "DISTRIBUTE TESTS PHASE": Goes over the tests in the active_test_list and distributes these tests among the available workers <-- ###
    for test in active_test_list:
        try:
            assigned_worker = active_worker_list[0]
            assigned_worker.assigned_test(test.TestID)
            test.assigned_worker(assigned_worker.WorkerID)
            active_worker_list.remove(assigned_worker)
            active_test_list.remove(test)
        except:
            pass
#### END SIMULATION ####

for x in Test.instances:
    print(x)
