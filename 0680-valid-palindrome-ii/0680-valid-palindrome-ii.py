class Solution:
    def validPalindrome(self, s: str) -> bool:


        def help(st, i, j, del_allowed):

            while i < j:


                if s[i] != s[j]:

                    if del_allowed == 0:
                        return False

                    return help(st, i+1,j, del_allowed -1) or help(st, i,j-1, del_allowed -1)

                i += 1
                j -= 1

            return True


        return help(s, 0, len(s)-1, 1)



