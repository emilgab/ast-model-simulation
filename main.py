# Classes
class Worker:
    def __init__(self, WorkerID, StartTimeAvailable, PerformanceRating, AvailabilityTime):
        self.WorkerID = str(WorkerID)
        self.StartTimeAvailable = float(StartTimeAvailable)
        self.PerformanceRating = float(PerformanceRating)
        self.AvailabilityTime = float(AvailabilityTime)
    def __str__(self):
        return f"{self.WorkerID}: \n\tStarted working: {self.StartTimeAvailable}\
        \n\tPerformance: {self.PerformanceRating*100}%\
        \n\tRemaining availability: {self.AvailabilityTime}"

class Test:
    def __init__(self, TestID, ScheduledTime, TestTime):
        self.TestID = str(TestID)
        self.ScheduledTime = float(ScheduledTime)
        self.TestTime = float(TestTime)
    def __str__(self):
        return f"{self.TestID}: \n\tScheduled for testing at: {self.ScheduledTime}\
        \n\tTime it takes for testing: {self.TestTime}"

#### PRE-FACE ####
# Start Time
time = 0.00

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
##################
