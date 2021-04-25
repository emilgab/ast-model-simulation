# Libraries #
import time # used for measuring completion times
import unittest # used for running unit tests
import multiprocessing as mp # used to run processes in paralell

# Stores unit test suites in a list used later for iteration
suites = []
# processing external unit tests #
# 1: Imports the unit tests classes from external scripts
from unittests import io, calculations, strings
# 2: Creates test suites from every class
suites.append(unittest.TestLoader().loadTestsFromModule(io))
suites.append(unittest.TestLoader().loadTestsFromModule(calculations))
suites.append(unittest.TestLoader().loadTestsFromModule(strings))
####

class Worker:
    counter = 0
    def __init__(self, cores):
        self.cores = cores
        self.id = self.give_id()

    def __str__(self):
        return f"{self.id}"

    def give_id(self):
        Worker.counter += 1
        id = "W"+str(Worker.counter).zfill(2)+f"-C{self.cores}"
        return id

    def run_unittest(self, test):
        pass

class TestInfrastructure:

    def __init__(self, cores):
        self.cores = cores
        self.id = "TestingInfrastructure1"

    def __str__(self):
        return f"{self.id}"

    def run_unittest(self, test):
        pass

# Flag 1: Getting start time for measuring completion times
start_time = time.monotonic_ns()

for suite in suites:
    # Runs the unit test suites with verbosity 0 (quiet)
    unittest.TextTestRunner(verbosity=0).run(suite)

# Flag 2: Getting the stop time for measuring completion times
end_time = time.monotonic_ns()
# Calculates the completion time in seconds instead of nanoseconds
completion_time_s = (end_time-start_time)/10**9
# Outputs the completion time
print("Completion time: ",completion_time_s)
