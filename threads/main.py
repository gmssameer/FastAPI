import threading
import time

class ThreadCounter:
    def __init__(self):
        self.count = 0

    def increment_and_print(self, thread_no:int):
        print(f"Thread {thread_no} started : count = {self.count}")
        self.count += 1
        time.sleep(2)
        print(f"Thread {thread_no} finished : count = {self.count}")

tc = ThreadCounter()

for i in range(3):
    t = threading.Thread(target=tc.increment_and_print, args=(i,))
    t.start()


