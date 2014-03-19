#### EXAMPLE ##################################################################

from time import sleep
from threading import Thread
import random
import yappi

def test_function():
    pass

class T(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):                  # takes about 5 seconds
        for i in xrange(100):
            self.test_method()
            test_function()

    def test_method(self):
        sleep(random.random() / 10)

yappi.start()
#######################
threads = [T() for i in xrange(3)]
for t in threads:
    t.start()
for i in xrange(100):
    test_function()
for t in threads:
    t.join()
#######################
yappi.stop()
yappi.get_func_stats().sort("totaltime").print_all()
yappi.get_thread_stats().sort("totaltime").print_all()