import threading
import time


def producer():
    with lock:
        print('done')
        with lock:
            print("It's great")
    print('Locking release!')


lock = threading.Lock()
# __enter__ => lock.acquire()
# __exit__ => lock.release()

task1 = threading.Thread(target=producer)
task2 = threading.Thread(target=producer)

task1.start()
task2.start()

task1.join()
task2.join()
