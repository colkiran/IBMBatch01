
from collections import namedtuple

def ArithmeticCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    nmdTpl = namedtuple("Arithmetic", "add sub mul div")
    arith = nmdTpl(add= sum, sub=diff, mul = prod, div = quot)
    return arith

res = ArithmeticCalc(20, 8)
print(f"res :{res}")
print(f"Add :{res.add}")
print(f"Sub :{res.sub}")
print(f"Mul :{res.mul}")
print(f"Div :{res.div}")

# immutable dictionary
# res.add = 500