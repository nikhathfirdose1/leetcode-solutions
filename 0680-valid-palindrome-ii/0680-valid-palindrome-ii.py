class Solution:
    def validPalindrome(self, s: str) -> bool:
        

        def isPal(i,j):

            while i < j:
                if s[i] != s[j]:
                    return False
            
                else:
                    i += 1
                    j -= 1

            return True

        i = 0
        j = len(s) - 1

        while i < j:

            if s[i] != s[j]:
                return isPal(i+1,j) or isPal(i, j-1)

            else:
                i += 1
                j -= 1

        return True
        
