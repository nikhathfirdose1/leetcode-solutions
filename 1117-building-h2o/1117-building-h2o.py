import threading

class H2O:
    def __init__(self):
        self.barrier = threading.Barrier(3, action= self.reset)
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)
        self.hydro = 0
        self.oxy = 0


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        
        with self.condition:
            while self.hydro == 2:
                self.condition.wait()

            
            releaseHydrogen()
            self.hydro += 1
            self.condition.notify_all()

        self.barrier.wait()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        
        with self.condition:
            while self.oxy == 1 or self.hydro <2 : 
                self.condition.wait()

            
            releaseOxygen()
            self.oxy += 1
            self.condition.notify_all()

        self.barrier.wait()

    
    def reset(self):

        with self.condition:
            self.hydro = 0
            self.oxy = 0
            self.condition.notify_all()

