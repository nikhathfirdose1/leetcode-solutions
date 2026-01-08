from threading import Event

class Foo:
    def __init__(self):
        self.firstD = Event()
        self.secondD = Event()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        printFirst()
        self.firstD.set()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        if self.firstD.wait():
            printSecond()
            self.secondD.set()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        if self.secondD.wait():
            printThird()