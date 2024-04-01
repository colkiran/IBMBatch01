
def greet():
    print(f"Greetings Mr. Sachin, Welcome to the event.......")

def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event......")

# city is the default argument and gname is non default argument
def greetGstCty(gname, city="Mumbai"):
    print(f"Greetings Mr.{gname} from {city}, Welcome to the event.......")

greet()

print("-" * 60)
greetGst("Rahul")

print("-" * 60)
greetGstCty("Sachin", 10)

print("-" * 60)
greetGstCty("Rohit", 20)

print("-" * 60)
greetGstCty("Rahul", "Bangalore")

# functions can return a value

def fun():
    return "hello world"

res = fun()
print(f"res :{res}")

# python supports recursive calls
# using recursive calls write a code to generate
# a. factorial of a  number
# b. fibanocci series

def fact(n):
    if n==0:
        return 1
    else:
        return n * fact(n-1)

print(f"the factorial of fact(5) is {fact(5)}")

print("=" * 60)
def fibo(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

iter = int(input("Enter the num of fibo numbers to be generated :"))
for i  in range(iter):
    print(fibo(i), end=" ")
print()