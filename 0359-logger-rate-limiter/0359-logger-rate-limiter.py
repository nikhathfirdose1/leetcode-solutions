class Logger:

    def __init__(self):

        self.hm = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:

        if message in self.hm:
            if self.hm[message] > timestamp:
                return False

        self.hm[message] = timestamp + 10
        return True

        
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)