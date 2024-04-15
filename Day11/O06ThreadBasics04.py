
import time
import threading
import concurrent.futures

st = time.perf_counter()

def doJob(secs):
    print(f"Sleeping for {secs} secs..............{threading.current_thread().name}")
    time.sleep(3)
    print(f"Just woke up.......{threading.current_thread().name}")

with concurrent.futures.ThreadPoolExecutor() as executor:
    thrd1 = executor.submit(doJob, 3)
    thrd2 = executor.submit(doJob, 3)
    thrd3 = executor.submit(doJob, 3)

et = time.perf_counter()
print(f"The total time taken to execute is {round(et - st, 2)}")
