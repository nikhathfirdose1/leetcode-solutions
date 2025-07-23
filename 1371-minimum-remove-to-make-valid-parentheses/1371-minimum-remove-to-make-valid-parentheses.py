class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack = []
        to_remove = set()

        for i,w in enumerate(s):

            if w == "(":
                stack.append(i)

            if w == ")":
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)

        to_remove.update(stack)

        res = []

        for i, c in enumerate(s):
            if i not in to_remove:
                res.append(c)
        
        return "".join(res)





        


            
        