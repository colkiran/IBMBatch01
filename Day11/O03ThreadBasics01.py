
import time

st = time.perf_counter()

def doJob():
    print("Sleeping for 3 secs")
    time.sleep(3)
    print("Just woke up.......")


doJob()
doJob()
doJob()

et = time.perf_counter()
print(f"The total time taken to execute is {round(et - st, 2)}")
