
def fun(*args):
    print(args)

fun()

fun(1)

fun(1, 2)

fun(1, 2, 3)
print("-" * 60)

def withdraw():
    print("debit")
def deposit():
    print("credit")

def helper(fnc):
    print("Logging into the sever.....")
    fnc()
    print("Logging out of the sever.....")
    print("-" * 60)

helper(withdraw)
helper(deposit)

