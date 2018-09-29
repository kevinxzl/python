from threading import Thread, Event
import time

# Code to execute in an independent thread


def countdown(n, started_evt):
    print('1 new thread starting --- countdown starting')
    started_evt.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(1)


# Create the event object that will be used to signal startup
started_evt = Event()

# Launch the thread and pass the startup event
print('Launching new thread --- countdown')
t = Thread(target=countdown, args=(10, started_evt))
t.start()

# Wait for the thread to start
"""
当你执行这段代码，“1 countdown is running” 总是显示在 “countdown starting” 之后显示。这是由于使用 event 来协调线程，使得主线程要等到 countdown() 函数输出启动信息后，才能继续执行。
"""
started_evt.wait()
print('2 new thread --- countdown is running')
