import threading
import time

items = [2, 4, 5, 2, 1, 7]


# just fun
def sleep_sort(i):
    time.sleep(i)
    print(i)


ts = [threading.Thread(target=sleep_sort, args=(i,)) for i in items]
[t.start() for t in ts]
