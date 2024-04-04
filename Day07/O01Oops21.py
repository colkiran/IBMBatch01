
from abc import ABC, abstractmethod

class Accounts(ABC):
    def __init__(self):
        print("Account....")

    def deposit(self):
        pass
    @abstractmethod
    def get_balance(self):
        pass

class Savings(Accounts):
    def withDraw(self):
        print("Amount XXXXXX debited from the account....")
    def get_balance(self):
        print("The balance in the account is  ####.##")

sa = Savings()

class CurrentAcount:

    def get_balace(self):
        print("Balance in the accout ")

ca = CurrentAcount()






