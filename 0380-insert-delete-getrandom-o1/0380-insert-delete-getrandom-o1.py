class RandomizedSet:

    def __init__(self):

        self.list = []
        self.hm = {}
        

    def insert(self, val: int) -> bool:

        if val in self.hm:
            return False


        self.list.append(val)
        self.hm[val] = len(self.list) - 1
        return True
        
    def remove(self, val: int) -> bool:

        if val not in self.hm:
            return False

        
        idx = self.hm[val]
        last_idx = len(self.list) -1
        last_val = self.list[last_idx]

        self.list[idx], self.list[last_idx] = self.list[last_idx], self.list[idx]

        self.list.pop()
        self.hm[last_val] = idx
        del self.hm[val]

        return True


        

    def getRandom(self) -> int:

        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()