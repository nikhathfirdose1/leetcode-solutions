class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        idx = len(num) - 1
        carry = 0
        res = []

        while idx >= 0 or k > 0:

            last = k % 10
            k = k // 10 
            
            if idx >= 0:
                d1 = num[idx]
            else:
                d1 = 0

            value = (d1 + last + carry) % 10
            carry = (d1 + last + carry) // 10

            idx -= 1

            res.append(value)


        if carry != 0:
            res.append(carry)

        return res[::-1]
