class Solution:
    def myPow(self, x: float, n: int) -> float:


        def recurse(num, power):

            if power == 0:
                return 1.0

            if num == 0:
                return 0

            if power % 2 == 0:

                return recurse(num*num, power//2)
            
            else:
                return num * recurse(num*num, (power-1)//2)


        res = recurse(x,abs(n))

        return res if n>= 0 else 1/res
        