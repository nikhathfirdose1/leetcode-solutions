class Solution:
    def isPalindrome(self, s: str) -> bool:



        def check_alpha(st):

            if ord("a") <= ord(st) <= ord("z"):

                return True

            elif ord("A") <= ord(st) <= ord("Z"):

                return True

            elif ord("0") <= ord(st) <= ord("9"):
                return True

            else:
                return False

            return False
        
        left = 0
        right = len(s) - 1

        while left <= right:

            while left < right and not check_alpha(s[left]):
                left += 1

            while left < right and not check_alpha(s[right]):
                right -= 1


            if s[left].lower() != s[right].lower():   
                return False

            
            left += 1
            right -= 1


        return True



