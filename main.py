import numpy as np
# Classes
class Worker:
    instances = []
    def __init__(self, WorkerID, StartTimeAvailable, PerformanceRating, AvailabilityTime):
        self.WorkerID = str(WorkerID)
        self.StartTimeAvailable = float(StartTimeAvailable)
        self.PerformanceRating = float(PerformanceRating)
        self.AvailabilityTime = float(AvailabilityTime)
        self.JoinedTesting = False
        self.AssignedWork = False
        self.AssignedTest = None
        self.CompletedTests = []
        self.NumberOfCompletedTests = len(self.CompletedTests)
        self.WorkingIntervals = []
        self.WaitingIntervals = []
        self.checkpoint = None
        self.TotalWaitTime = sum(self.WaitingIntervals)
        self.instances.append(self)

    def __str__(self):
        return f"{self.WorkerID}: \n\tStarted working: {self.StartTimeAvailable}\
        \n\tPerformance: {round(self.PerformanceRating*100)}%\
        \n\tRemaining availability: {self.AvailabilityTime}\
        \n\tJoinedTesting: {'Yes' if self.JoinedTesting else 'No'}\
        \n\tAvailable to work at current time ({time}): {'Yes' if self.AssignedWork == False and self.JoinedTesting else 'No'}\
        \n\tAssigned Test: {self.AssignedTest if self.AssignedTest else 'None'}\
        \n\tCompleted Tests: {' '.join(self.CompletedTests)}\
        \n\tCompleted Tests count: {str(len(self.CompletedTests))}\
        \n\tWaiting Time List: {self.WaitingIntervals}\
        \n\tTest statistics:\
        \n\tTest distribution min: {str(np.min(self.WorkingIntervals)) if bool(self.WorkingIntervals) else 'N/A' } \
        \n\tTest distribution median: {str(np.median(self.WorkingIntervals)) if bool(self.WorkingIntervals) else 'N/A'}\
        \n\tTest distribution mean: {str(np.mean(self.WorkingIntervals)) if bool(self.WorkingIntervals) else 'N/A'}\
        \n\tTest distribution 75%: {str(np.percentile(self.WorkingIntervals,75)) if bool(self.WorkingIntervals) else 'N/A'}\
        \n\tTest distribution max: {str(np.max(self.WorkingIntervals)) if bool(self.WorkingIntervals) else 'N/A'}\
        \n\tWait interval statistics:\
        \n\tWait distribution min: {str(np.min(self.WaitingIntervals)) if bool(self.WaitingIntervals) else 'N/A'}\
        \n\tWait distribution median: {str(np.median(self.WaitingIntervals)) if bool(self.WaitingIntervals) else 'N/A'}\
        \n\tWait distribution mean: {str(np.mean(self.WaitingIntervals)) if bool(self.WaitingIntervals) else 'N/A'}\
        \n\tWait distribution 75%: {str(np.percentile(self.WaitingIntervals,75)) if bool(self.WaitingIntervals) else 'N/A'}\
        \n\tWait distribution max: {str(np.max(self.WaitingIntervals)) if bool(self.WaitingIntervals) else 'N/A'}\
        \n\tTotal wait time: {self.TotalWaitTime}"
    def assigned_test(self, test):
        self.AssignedWork = True
        self.AssignedTest = test_overview_dictionary[test].TestID
        original_testtime = test_overview_dictionary[test].TestTime
        number_after_performance = round((float(original_testtime)*60) / float(self.PerformanceRating))
        test_overview_dictionary[test].TestTime = float(f"{number_after_performance//60}.{number_after_performance%60}")
        # append the time differenece since we finished the last test to "WaitingIntervals"
        self.WaitingIntervals.append(self.time_diff(time,self.checkpoint))
        # set new checkpoint
        self.checkpoint = time

    def process(self):
        self.AvailabilityTime -= 1
        if self.AvailabilityTime > 0:
            if self.AssignedTest:
                test_overview_dictionary[self.AssignedTest].TestTime -= 1
                if test_overview_dictionary[self.AssignedTest].TestTime < 1 and test_overview_dictionary[self.AssignedTest].TestTime != 0:
                    test_overview_dictionary[self.AssignedTest].TestTime = 1
                elif test_overview_dictionary[self.AssignedTest].TestTime == 0:
                    self.CompletedTests.append(test_overview_dictionary[self.AssignedTest].TestID)
                    self.AssignedTest = None
                    self.WorkingIntervals.append(self.time_diff(time,self.checkpoint))
                    self.checkpoint = time
            else:
                self.AssignedWork = False
                self.TotalWaitTime += 1
        else:
            finished_workers.append(self)
            self.JoinedTesting = False

    def time_diff(self, original, subtraction):
        orig = original.split(".")
        subs = subtraction.split(".")
        origminutes = int(orig[0]) * 60 + int(orig[1])
        subminutes = int(subs[0]) * 60 + int(subs[1])
        return int(origminutes - subminutes)

class Test:
    instances = []
    def __init__(self, TestID, ScheduledTime, TestTime):
        self.TestID = str(TestID)
        self.ScheduledTime = ScheduledTime
        self.TestTime = float(TestTime)
        self.AssignedWorker = "N/A"
        self.WaitTime = None
        self.instances.append(self)
    def __str__(self):
        return f"{self.TestID}: \n\tScheduled for testing at: {self.ScheduledTime}\
        \n\tTime it takes for testing: {self.TestTime}\
        \n\tAssigned to worker: {self.AssignedWorker}\
        \n\tThis test waited in queue for: {self.WaitTime}"

    def assigned_worker(self, worker):
        self.AssignedWorker = worker
        if float(time) == float(self.ScheduledTime):
            self.WaitTime = 0
        else:
            self.WaitTime = self.time_diff(time,self.ScheduledTime)

    def time_diff(self, original, subtraction):
        orig = original.split(".")
        subs = subtraction.split(".")
        origminutes = int(orig[0]) * 60 + int(orig[1])
        subminutes = int(subs[0]) * 60 + int(subs[1])
        return int(origminutes - subminutes)

### PRE-PHASE ###

# Uses list comprehension to create the 24 hours (0-23).
hrs = [str(x).zfill(2) for x in range(0,24)]

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
test_scenario = "tasklists/continuous_intense.csv"

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

# Creates duplicate dictoinaries that will be used later for referencing
worker_overview_dictionary = dict(worker_dictionary_queue)
test_overview_dictionary = dict(test_dictionary_queue)

# Following lists will contain the active tests and workers at any given time based on the times in the tasklists and workerlists
active_worker_list = []
active_test_list = []

finished_workers = []
finished_tests = []

# This dictionary will contain information regarding the completed tests.
completed_test_dictionary = {}

# Dictionary to keep track on how many available workers there are per time (Not working)
available_workers_per_round = {}

# Dictionary to keep track of the remaining tests per time
remaining_tests_per_time = {}

### END OF PRE-PHASE ###

### SIMULATION ###
### |
# Iterates through the times of the day
for time in times:
    ### --> SIMULATION "WORK ON TEST"-PHASE: Every worker will process the tests they are assigned by "1" (representing 1 minute)
    for key,value in worker_overview_dictionary.items():
        if value.JoinedTesting == True:
            value.process()
    ### --> SIMULATION "CHECK"-PHASE: Checking the queue dictionaries and adding them in the active lists <-- ###
    # Adds the tests scheduled for current time to the "active_tests_queue" from the "test_dictionary_queue"
    tests_to_remove_from_queue = []
    for key, value in test_dictionary_queue.items():
        if len(str(value.ScheduledTime))==3:
            value.ScheduledTime = "0"+(str(value.ScheduledTime)+"0")
        if str(value.ScheduledTime).zfill(5) == time:
            active_test_list.append(value)
            tests_to_remove_from_queue.append(key)
    for item in tests_to_remove_from_queue:
        del test_dictionary_queue[item]
    # Adds the available workers to active workers list from the worker_dictionary_queue.
    workers_to_remove_from_queue = []
    for key, value in worker_dictionary_queue.items():
        if len(str(value.StartTimeAvailable)) < 5:
            if len(str(value.StartTimeAvailable))==3:
                value.StartTimeAvailable = "0"+(str(value.StartTimeAvailable)+"0")
            elif len(str(value.StartTimeAvailable).split(".")[-1]) == 2:
                value.StartTimeAvailable = str(value.StartTimeAvailable).zfill(5)
            elif len(str(value.StartTimeAvailable).split(".")[-1]) == 1:
                value.StartTimeAvailable = str(value.StartTimeAvailable).ljust(5,"0")
        if str(value.StartTimeAvailable).zfill(5) == time:
            active_worker_list.append(value)
            worker_overview_dictionary[key].JoinedTesting = True
            worker_overview_dictionary[key].checkpoint = time
            workers_to_remove_from_queue.append(key)
    for item in workers_to_remove_from_queue:
        del worker_dictionary_queue[item]
    ### END "CHECK"-PHASE ###
    ### |
    ### |
    ### |
    ### --> SIMULATION "CHECK FOR AVAILABLE WORKERS PHASE": Checks for workers that are finished working and are now available <-- ###
    for key, value in worker_overview_dictionary.items():
        if value.AssignedWork == False and value not in active_worker_list and value.JoinedTesting == True:
            active_worker_list.append(value)
    ### END "CHECK FOR AVAILABLE WORKERS PHASE" ###
    ### |
    ### |
    ### |
    ### --> Check for available workers and appends this value, with the time, in the dictoinary "available_workers_per_round"
    available_workers_per_round[time] = len(active_worker_list)
    ### --> End <--
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
    ### END SIMULATION "DISTRIBUTE TESTS PHASE"
    ### |
    ### |
    ### |
    ### --> Check the remaining tests and adds this information to the dictionary "remaining_tests_per_time"
    remaining_tests_per_time[time] = len(active_test_list)
#### END SIMULATION ####
