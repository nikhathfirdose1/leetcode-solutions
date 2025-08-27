class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        res = []

        def backtrack(o,c):

            if o == c == n:
                
                return res.append("".join(stack))

            if o < n:
                stack.append("(")
                backtrack(o+1, c)
                stack.pop()

            if c < o:
                stack.append(")")
                backtrack(o, c+1)
                stack.pop()

            return res

        return backtrack(0,0)

        