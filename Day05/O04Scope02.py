
def fun(x, y):
    # x y and z are all local variables
    print(f"x + y :{x + y}")
    z = x + y
    print(f"z :{z}")

fun(10, 20)
print(f"z :{z}")
