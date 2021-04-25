# Libraries #
import time # used for measuring completion times
import unittest # used for running unit tests

# processing external unit tests #
# 1: Imports the unit tests classes from external scripts
from unittests import io, calculations, strings
# 2: Creates test suites from every class
io_suite = unittest.TestLoader().loadTestsFromModule(io)
calculations_suite = unittest.TestLoader().loadTestsFromModule(calculations)
strings_suite = unittest.TestLoader().loadTestsFromModule(strings)
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

# Runs the unit test suites with verbosity 0 (quiet)
unittest.TextTestRunner(verbosity=0).run(io_suite)
unittest.TextTestRunner(verbosity=0).run(calculations_suite)
unittest.TextTestRunner(verbosity=0).run(strings_suite)

# Flag 2: Getting the stop time for measuring completion times
end_time = time.monotonic_ns()
# Calculates the completion time in seconds instead of nanoseconds
completion_time_s = (end_time-start_time)/10**9
# Outputs the completion time
print("Completion time: ",completion_time_s)
