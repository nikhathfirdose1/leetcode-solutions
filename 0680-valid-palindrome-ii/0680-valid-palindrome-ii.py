class Solution:
    def validPalindrome(self, s: str) -> bool:


        def help(st, i, j):

            while i < j:

                if st[i] != st[j]:
                    return False

                i += 1
                j -= 1

            return True


        i = 0 
        j = len(s) - 1

        while i < j:

            if s[i] != s[j]:
                return help(s, i+1, j) or help(s, i,j-1)

            i += 1
            j -= 1

        return True




