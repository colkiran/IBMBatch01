

def BankFun(fnc):
    def helper(amt):
        print("Logging into the system.....")
        fnc(amt)
        print("Logging out of the sh=ystem......")
        print("-" * 60)

    return helper

@BankFun            # deposit = BankFun(deposit)
def deposit(amt):
    print(f"credited {amt} into account no. ending XXXX")

@BankFun
def withdraw(amt):
    print(f"debited {amt} from account no. ending XXXX")


deposit(25000)
withdraw(8500)
