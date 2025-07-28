class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        sign = "+"
        s = s.replace(" ", "")
        num = 0

        for i, c in enumerate(s):

            if c.isdigit():
                num = num * 10 + int(c)

            if c in "+-*/" or i == len(s) - 1:

                if sign == "+":
                    stack.append(num)
                
                elif sign == "-":
                    stack.append(-num)

                elif sign == "*":
                    prev = stack.pop()
                    res = num * prev
                    stack.append(res)

                elif sign == "/":
                    prev = stack.pop()
                    res = int(prev / num)
                    stack.append(res)

                
                sign = c
                num = 0

        
        return sum(stack)
                


        