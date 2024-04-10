import time
def timeCalc(fnc):
    def helper(x):
        print("Executing the function......")
        st = time.time()
        fnc(x)
        et = time.time()
        print("Completed executing......")
        print(f"The total time taken by the function to execute :{et - st}")
        print("-" * 60)

    return helper

@timeCalc
def fun(val):
    lst = []
    for i in range(1, val+1):
        for j in range(1, i+1):
            lst.append(j ** 3)

fun(6000)
