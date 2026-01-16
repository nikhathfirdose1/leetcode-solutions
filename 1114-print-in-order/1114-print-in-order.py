import threading

class Foo:
    def __init__(self):
        self.lock = threading.Lock()
        self.cond = threading.Condition(self.lock)
        self.flag = "first"


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        with self.lock:
            while self.flag != "first":
                self.cond.wait()
            
            printFirst()
            self.flag = "sec"
            self.cond.notify_all()
        


    def second(self, printSecond: 'Callable[[], None]') -> None:

        with self.lock:
            while self.flag != "sec":
                self.cond.wait()
            
            printSecond()
            self.flag = "third"
            self.cond.notify_all()


    def third(self, printThird: 'Callable[[], None]') -> None:

        with self.lock:
            while self.flag != "third":
                self.cond.wait()
            
            printThird()
            self.cond.notify_all()