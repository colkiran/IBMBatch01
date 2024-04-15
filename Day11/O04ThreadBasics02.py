

import time
import threading

st = time.perf_counter()

def doJob():
    print("Sleeping for 3 secs")
    time.sleep(3)
    print("Just woke up.......")


thrd1 = threading.Thread(target=doJob, name="t1")
thrd2 = threading.Thread(target=doJob, name="t2")
thrd3 = threading.Thread(target=doJob, name="t3")

thrd1.start()
thrd2.start()
thrd3.start()

thrd1.join()        # will tell the main thread to wait for t1 to complete
thrd2.join()
thrd3.join()

et = time.perf_counter()
print(f"The total time taken to execute is {round(et - st, 2)}")

import os
print(os.cpu_count())       # 8 cores - 8 threads parallely
