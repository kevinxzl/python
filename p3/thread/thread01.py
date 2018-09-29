# Code to execute in an independent thread
import time
from threading import Thread


def countdown(n):
    while n > 0:
        print('new thread:T-minus', n)
        n -= 1
        time.sleep(1)


# Create and launch a thread
t = Thread(target=countdown, args=(5,))
t.start()
print("This is main thread")

if t.is_alive():
    print('new thread is still running')
else:
    print('new thread Completed')

time.sleep(6)
if t.is_alive():
    print('new thread is still running')
else:
    print('new thread Completed')
