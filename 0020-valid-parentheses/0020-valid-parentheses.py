class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        hm = {"}" : "{", ")": "(", "]": '['}

        for c in s:
            if c in hm:
                if not stack or stack[-1] != hm[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
                
        
        return not stack
                    
        