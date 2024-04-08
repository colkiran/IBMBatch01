
num = 10
div = 0

try:
    assert div != 0, "Invalid Operation"
    print(num / div)

except AssertionError as msg:
    print(msg)
