from threading import Lock
from threading import Condition


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.turn = "zero"
        self.lock = Lock()
        self.cond = Condition(self.lock)
        self.i = 1
        
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n):
            with self.cond:
                while self.turn != "zero":
                    self.cond.wait()

                printNumber(0)
                if self.i % 2 != 0:
                    self.turn = "odd"
                else:
                    self.turn = "even"
                
                self.cond.notify_all()
        


        
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:

        for _ in range((self.n)//2):
            with self.cond:
                while self.turn != "even":
                    self.cond.wait()

                printNumber(self.i)
                self.i += 1
                self.turn = "zero"

                self.cond.notify_all()


    def odd(self, printNumber: 'Callable[[int], None]') -> None:

        for _ in range((self.n+1)//2):
            with self.cond:
                while self.turn != "odd":
                    self.cond.wait()

                printNumber(self.i)
                self.i += 1
                self.turn = "zero"

                self.cond.notify_all()
    

        
        