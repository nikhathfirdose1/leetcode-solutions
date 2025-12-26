class RandomizedSet:

    def __init__(self):
        self.list = []
        self.hm = {}

    def insert(self, val: int) -> bool:

        if val not in self.hm:
            self.list.append(val)
            self.hm[val] = len(self.list) - 1
            return True
        else:
            return False 

    def remove(self, val: int) -> bool:

        if val in self.hm:

            idx = self.hm[val]
            value = self.list[-1]

            self.list[self.hm[val]], self.list[-1] = self.list[-1], self.list[self.hm[val]]

            self.hm[value] = idx

            self.list.pop()

            del self.hm[val]


            return True
        else:
            return False
        

    def getRandom(self) -> int:
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()