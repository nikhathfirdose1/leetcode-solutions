from threading import Semaphore

class Foo:
    def __init__(self):

        self.a = Semaphore(1)
        self.b = Semaphore(0)
        self.c = Semaphore(0)

        pass


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        self.a.acquire()
        printFirst()
        self.b.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        self.b.acquire()
        printSecond()
        self.c.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        self.c.acquire()
        printThird()
        self.a.release()