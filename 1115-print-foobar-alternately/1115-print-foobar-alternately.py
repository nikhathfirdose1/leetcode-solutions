import threading

class FooBar:
    def __init__(self, n):
        self.n = n
        self.lock = threading.Lock()
        self.cond = threading.Condition(self.lock)
        self.turn = "foo"



    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            with self.cond:
                while self.turn == "bar":
                    self.cond.wait()
                printFoo()
                self.turn = "bar"
                self.cond.notify_all()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            with self.cond:
                while self.turn == "foo":
                    self.cond.wait()
                
                printBar()
                self.turn = "foo"
                self.cond.notify_all()