
# nested functions

def outerFun(gname):
    print(f"outerfun before :{gname}")
    def innerFun():
        nonlocal gname
        gname = "Mr." + gname
        print("Hello World")
        print(f"Greetings {gname}")

    # outerfun
    innerFun()
    print(f"outerFun after :{gname}")

outerFun("Sachin")