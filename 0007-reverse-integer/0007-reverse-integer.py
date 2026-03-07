class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        MAX_PREFIX = 214748364
        MIN_PREFIX = -214748364

        rev = 0

        while x != 0:
            digit = x % 10

            if x < 0 and digit > 0:
                digit -= 10

            x = (x - digit) // 10

            if rev > MAX_PREFIX or (rev == MAX_PREFIX and digit > 7):
                return 0
            if rev < MIN_PREFIX or (rev == MIN_PREFIX and digit < -8):
                return 0

            rev = rev * 10 + digit

        return rev