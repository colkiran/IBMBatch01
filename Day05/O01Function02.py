
def ArithmeticCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

res = ArithmeticCalc(20, 8)
print(f"res :{res}")

print("-" * 60)
# variable length arguments - *args, **kwargs

# variable is prefixed with a * then it can accept more than one value
def prodAll(*numbers):
    print(numbers)
    print(*numbers)
    Prod = 1
    for number in numbers:
        Prod *= number
    return Prod


res = prodAll(1, 2, 3, 4, 5)
print(f"res :{res}")

print("-" * 60)

# **kwargs - var prefixed with two stars will store data in a dictionary
def extractDetails(**details):
    print(details)
    for k, v in details.items():
        print(k + "=>" + str(v))

extractDetails(name="Sachin", age=32, runs=92, oppon="SA")

print("-" * 60)

def fun():
    "this is a doc string"
    # this is a comment
    print("Hello World")

fun()
print(fun.__doc__)

print("-" * 60)

def fun1(x, y):
    """
    fun1 takes two arguments
        1. if both the arguments are numbers then the output will be the sum of both
        2. if both the arguments are strings then the output will be the concatenated
        3. if the data passed is of two different data types then an error is raised
    """
    return x + y

res = fun1(10, 20)
print(f"res :{res}")
print("=" * 60)

help(fun1)
