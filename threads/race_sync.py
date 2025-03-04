import logging
import threading
import time

import concurrent.futures

'''
use thread to create concurency in puthon and use lock to avoid race condition
'''

class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def update(self, name):
        logging.info("Thread %s: starting update lock", name)
        with self._lock:
            local_copy = self.value
            local_copy += 1
            print(f"Local copy before update {local_copy} in thread {name}")
            time.sleep(1)
            self.value = local_copy
            print(f"Value updated {self.value} in thread {name}")
        
        logging.info("Thread %s: finishing update lock", name)

#the name is set as  main if the its run as script
if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    database = FakeDatabase()
    logging.info("Testing update. Starting value is %d.", database.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        for index in range(3):
            executor.submit(database.update, index)
    logging.info("Testing update. Ending value is %d.", database.value)
