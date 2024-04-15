

import time
import threading

st = time.perf_counter()

def doJob(secs, tname):
    print(f"Sleeping for {secs} secs ---------------- {tname}")
    time.sleep(secs)
    print(f"Just woke up after {secs}.......{tname}")

threads = []
for i in range(10):
    t = threading.Thread(target=doJob, name="t"+ str(i), args=[3, "thrd-" + str(i)])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

et = time.perf_counter()
print(f"The total time taken to execute is {round(et - st, 2)}")

import os
print(os.cpu_count())       # 8 cores - 8 threads parallely
