import threading


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.i = 1
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:

        while True:
            with self.condition:
                while self.i <= self.n and (self.i % 3 != 0 or self.i % 5 == 0):
                    self.condition.wait()
                
                if self.i > self.n:
                    self.condition.notify_all()
                    return
                
                printFizz()
                self.i += 1
                self.condition.notify_all()
    	

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:

        while True:
            with self.condition:
                while self.i <= self.n and (self.i % 5 != 0 or self.i % 3 == 0):
                    self.condition.wait()
                
                if self.i > self.n:
                    self.condition.notify_all()
                    return
                
                printBuzz()
                self.i += 1
                self.condition.notify_all()
    	

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:

        while True:
            with self.condition:
                while self.i <= self.n and (self.i % 15 != 0):
                    self.condition.wait()
                
                if self.i > self.n:
                    self.condition.notify_all()
                    return
                
                printFizzBuzz()
                self.i += 1
                self.condition.notify_all()
        

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:

        while True:
            with self.condition:
                while self.i <= self.n and (self.i % 3 == 0 or self.i % 5 == 0):
                    self.condition.wait()
                
                if self.i > self.n:
                    self.condition.notify_all()
                    return
                
                printNumber(self.i)
                self.i += 1
                self.condition.notify_all()
        