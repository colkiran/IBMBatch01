def outerFun(gname):        #HOF - Higher Order Function
    def innerFun():
        print(f"Greeting Mr.{gname}, Welcome to the event.....")

    return innerFun


inref = outerFun("Sachin")

# after few lines of code
# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")

inref()