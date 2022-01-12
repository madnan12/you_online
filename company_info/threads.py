import time
import threading
start=time.perf_counter()
seconds=0
def do_something():
    print((f'sleeping {seconds} seconds'))
    time.sleep(seconds)
    print('done sleeping')

threads=[]

for _ in range(10):
    t=threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)

finish=time.perf_counter()

for tread in threads:
    tread.join()

print(f'finish in {round(finish-start,2)} seconds')