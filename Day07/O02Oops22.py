
from abc import ABC, abstractmethod

class Employee(ABC):
    def doJob(self):
        pass

class Manager(Employee):
    def doJob(self):
        print("Managers Job.....")

class Developer(ABC):
    def doJob(self):
        print("Developers Job......")

def bankJob(emp):
    print("Back job Started.....")
    emp.doJob()
    print("Back job Ended....")
    print("-" * 60)

Mike = Manager()
Dave = Developer()


bankJob(Mike)
bankJob(Dave)