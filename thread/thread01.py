import time
import _thread

# Define a function for the thread


def func(string, sleeptime, lock, *args):
    while True:
        lock.acquire()
        time.sleep(sleeptime)
        lock.release()
        time.sleep(sleeptime)


def main():
    lock = _thread.allocate_lock()
    # Create two threads as follows
    try:
        _thread.start_new_thread(func, ("Thread  # : 1", 2, lock))
        _thread.start_new_thread(func, ("Thread  # : 2", 3, lock))

    except:
        print ("Error: unable to start thread")


main()
