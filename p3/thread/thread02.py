# Code to execute in an independent thread
import time
from threading import Thread


class CountdownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(5)


c = CountdownTask()
t = Thread(target=c.run, args=(10,))
t.start()
print("main thread will terminated new thread")
c.terminate()  # Signal termination
t.join()      # Wait for actual termination (if needed)

if t.is_alive():
    print('new thread is still running')
else:
    print('new thread Completed')
