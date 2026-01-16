import threading
class TrafficLight:
    def __init__(self):
        self.a_green = True
        self.lock = threading.Lock()

    def carArrived(
        self,
        carId: int,                      # ID of the car
        roadId: int,                     # ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
        direction: int,                  # Direction of the car
        turnGreen: 'Callable[[], None]', # Use turnGreen() to turn light to green on current road
        crossCar: 'Callable[[], None]'   # Use crossCar() to make car cross the intersection
    ) -> None:


        with self.lock:

            if roadId == 1:
                if self.a_green:
                    crossCar()
                else:
                    turnGreen()
                    crossCar()
                    self.a_green = True

            if roadId == 2:
                if not self.a_green:
                    crossCar()
                else:
                    turnGreen()

                    crossCar()
                    self.a_green = False


        

