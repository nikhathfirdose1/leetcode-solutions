class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        

        idx =[]
        rem = set()
        ans = []

        for i, w in enumerate(s):

            if w == "(":
                idx.append(i)

            if w == ")":
                if idx:
                    idx.pop()
                else:
                    rem.add(i)

        while idx:
            rem.add(idx.pop())

        for i, c in enumerate(s):
            if i not in rem:
                ans.append(c)


        return "".join(ans)
