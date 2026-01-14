from collections import defaultdict


class RandomizedCollection:

    def __init__(self):

        self.multiset = []
        self.hm = defaultdict(set)
        self.freq = defaultdict(int)
        

    def insert(self, val: int) -> bool:

        is_first = self.freq[val] == 0

        self.multiset.append(val)
        idx = len(self.multiset) - 1

        self.hm[val].add(idx)
        self.freq[val] = self.freq.get(val, 0) + 1

        return is_first

        

        

    def remove(self, val: int) -> bool:

        if self.freq[val] == 0:
            return False

        idx = self.hm[val].pop()

        last_idx = len(self.multiset) - 1
        last_val = self.multiset[last_idx]


        if idx != last_idx:


            self.multiset[idx], self.multiset[-1] = self.multiset[-1], self.multiset[idx]

            self.hm[last_val].remove(last_idx)
            self.hm[last_val].add(idx)

        self.multiset.pop()
        self.freq[val] = self.freq.get(val, 0) - 1

        if self.hm[val] == 0: # if set empty
            del self.hm[val]

        return True
        



        

    def getRandom(self) -> int:

        if self.multiset:
            return random.choice(self.multiset)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()