class Solution:
    def reverse(self, x: int) -> int:

      
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        rev = 0

        neg = False

        if x <0:
            x = -x
            neg = True
        
        while x != 0:
      
            digit = int(x % 10)

            x = (x) // 10
            
            
            if rev > INT_MAX // 10 or rev < INT_MIN // 10:
                return 0

            
            rev = rev * 10 + digit
        
        return rev if neg == False else -rev



