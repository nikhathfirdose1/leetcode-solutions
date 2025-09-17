# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:

        def bs(s,e):

            while s <= e:
                m = (s+e) // 2

                if reader.get(m) == target:
                    return m
                
                elif target < reader.get(m):
                    e = m - 1
                
                else:
                    s = m + 1

            return -1
        
        low = 0
        high = 1

        while reader.get(high) < target:
            low = high
            high *= 2

        return bs(low, high)
