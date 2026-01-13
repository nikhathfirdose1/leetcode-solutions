import random

class RandomizedSet:

    def __init__(self):

        self.items = []
        self.hm = {} 

    def insert(self, val: int) -> bool:

        if val not in self.hm:
            self.items.append(val)
            self.hm[val] = len(self.items) - 1
            return True
        
        return False
        

    def remove(self, val: int) -> bool:

        if val in self.hm:


            idx = self.hm[val]
            last_val = self.items[-1]


            self.items[idx], self.items[-1] =self.items[-1] , self.items[idx]
            
            self.hm[last_val] = idx
            

            self.items.pop()

            del self.hm[val]

            return True

        
        return False




    def getRandom(self) -> int:


        return random.choice(self.items)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()