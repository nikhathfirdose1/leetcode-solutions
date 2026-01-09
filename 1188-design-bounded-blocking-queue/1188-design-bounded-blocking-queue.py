from threading import Lock
from threading import Condition
from collections import deque

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):

        self.capacity = capacity
        self.my_queue = []
        self.lock = Lock()
        self.cond = Condition(self.lock)
        

    def enqueue(self, element: int) -> None:

        with self.cond:
            while len(self.my_queue) == self.capacity:
                self.cond.wait()
            

            self.my_queue.append(element)
            self.cond.notify_all()


    def dequeue(self) -> int:

        with self.cond:
            while len(self.my_queue) == 0:
                self.cond.wait()

            val = self.my_queue.pop(0)
            self.cond.notify_all()
            return val
        

    def size(self) -> int:
        
        with self.cond:
            return len(self.my_queue)