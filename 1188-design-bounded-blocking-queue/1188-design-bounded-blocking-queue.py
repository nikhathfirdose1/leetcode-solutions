import threading 

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):

        self.capacity = capacity
        self.queue = []
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)
        

    def enqueue(self, element: int) -> None:
        with self.condition:
            while self.capacity == self.size():
                self.condition.wait()

            self.queue.append(element)
            self.condition.notify_all()

            print(self.queue)

    def dequeue(self) -> int:
        
        with self.condition:
            while self.size() == 0:
                self.condition.wait()

            rear = self.queue[0]
            self.queue.remove(rear)
            self.condition.notify_all()

            return rear

    def size(self) -> int:

        return len(self.queue)
        