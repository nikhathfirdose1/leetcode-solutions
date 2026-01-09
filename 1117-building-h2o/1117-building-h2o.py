from threading import Lock, Condition, Barrier


class H2O:
    def __init__(self):

        self.barrier = Barrier(3)
        self.lock = Lock()
        self.cond = Condition(self.lock)
        self.hydro = 0
        self.oxy = 0
        pass


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        
        # releaseHydrogen() outputs "H". Do not change or remove this line.


        with self.cond:
            while self.hydro == 2:
                self.cond.wait()
            
            self.hydro += 1
            releaseHydrogen() 
            self.cond.notify_all()

        self.barrier.wait()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        
        # releaseOxygen() outputs "O". Do not change or remove this line.
        with self.cond:
            while self.hydro < 2 or self.oxy == 1:
                self.cond.wait()
        
            self.oxy += 1
            releaseOxygen()
            

        self.barrier.wait()

        with self.cond:
            self.hydro = 0
            self.oxy = 0
            self.cond.notify_all()
            