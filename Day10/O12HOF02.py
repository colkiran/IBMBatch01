
def sum(x, y):
    print("sum fnc called......")
    return x + y

def diff(x, y):
    print("diff fnc called.......")
    return x - y


def outerFun(fnc):

    def helper(*args):
        print("Logging in.....")
        print(fnc(*args))
        print("logging out.....")
        print("-" * 60)

    return helper

sumRef = outerFun(sum)
sumRef(10, 20)

difRef = outerFun(diff)
difRef(30, 12)
