from threading import Semaphore

class FooBar:
    def __init__(self, n):
        self.n = n
        self.a = Semaphore(1)
        self.b = Semaphore(0)


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.a.acquire()
            printFoo()
            self.b.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.b.acquire()
            printBar()
            self.a.release()