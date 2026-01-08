from threading import Lock

class Foo:
    def __init__(self):
        self.firstD = Lock()
        self.secondD = Lock()
        self.firstD.acquire()
        self.secondD.acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        printFirst()
        self.firstD.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        with self.firstD:
            printSecond()
            self.secondD.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        with self.secondD:
            printThird()