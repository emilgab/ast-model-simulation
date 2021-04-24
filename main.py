import random

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

class TestInfrastructure:
    
    def __init__(self, cores):
        self.cores = cores
        self.id = "TestingInfrastructure1"

    def __str__(self):
        return f"{self.id}"
