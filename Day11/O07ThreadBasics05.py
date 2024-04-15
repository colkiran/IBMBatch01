

import time
import threading
import concurrent.futures

st = time.perf_counter()

def doJob(secs):
    print(f"Sleeping for {secs} secs..............{threading.current_thread().name}")
    time.sleep(secs)
    print(f"Just woke up.......{threading.current_thread().name}")

with concurrent.futures.ThreadPoolExecutor() as executor:
   secs = [6, 5, 4, 3, 2, 1]
   executor.map(doJob, secs)


et = time.perf_counter()
print(f"The total time taken to execute is {round(et - st, 2)}")
