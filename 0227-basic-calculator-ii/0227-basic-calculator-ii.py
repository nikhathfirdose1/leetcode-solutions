class Solution:
    def calculate(self, s: str) -> int:

        last = 0
        sign = "+"
        s = s.replace(" ", "")
        num = 0
        res =0

        for i, c in enumerate(s):

            if c.isdigit():
                num = num * 10 + int(c)

            if c in "+-*/" or i == len(s) - 1:

                if sign == "+":
                    
                    res += last
                    last = num
                
                elif sign == "-":
                    
                    res += last
                    last = -num

                elif sign == "*":
                    last = num * last
                    
                elif sign == "/":
                    last = int(last / num)
    
                sign = c
                num = 0

        res += last  
        return res
                


        