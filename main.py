import time

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

start_time = time.monotonic_ns()



end_time = time.monotonic_ns()
completion_time_s = (end_time-start_time)/10**9
