# import time
# import threading
# start=time.perf_counter()
# seconds=0
# def do_something():
#     print((f'sleeping {seconds} seconds'))
#     time.sleep(seconds)
#     print('done sleeping')

# threads=[]

# for _ in range(10):
#     t=threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     threads.append(t)

# finish=time.perf_counter()

# for tread in threads:
#     tread.join()

# print(f'finish in {round(finish-start,2)} seconds')

from multiprocessing import Process, Lock
def dispmay_name(l, i):
    l.acquire()
    print ('Hi', i)
    l.release()
if __name__ == '__main__':
    my_lock = Lock()
    my_name = ['Aadrika', 'Adwaita', 'Sakya', 'Sanj']
for name in my_name:
    Process(target=dispmay_name, args=(my_lock,name)).start()