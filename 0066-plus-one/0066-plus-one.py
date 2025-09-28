class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        p = len(digits) - 1
        res = []
        carry = 0

        while p >= 0:

            if p == len(digits) - 1:
                value = (digits[p] + 1 + carry) % 10
                carry = (digits[p] + 1 +  carry) // 10

            else:
                value = (digits[p] + carry) % 10
                carry = (digits[p] +  carry) // 10

            res.append(value)

            p -= 1

        if carry != 0:
            res.append(carry)

        
        return res[::-1]



        
        