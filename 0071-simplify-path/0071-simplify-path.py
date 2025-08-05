class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []
        ans = ""

        for val in path.split("/"):
            if val == "..":
                if stack:
                    stack.pop()
            
            elif val == "." or val == "":
                continue
            
            else:
                stack.append(val)

        return "/" + "/".join(stack)

            