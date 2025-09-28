class Solution:
    def addBinary(self, a: str, b: str) -> str:

        carry = 0
        res = 0

        p1 = len(a) - 1
        p2 = len(b) - 1

        res = []

        while p1 >= 0 or p2 >= 0:

            x1 = ord(a[p1]) - ord("0") if p1>= 0 else 0
            x2 = ord(b[p2]) - ord("0") if p2 >= 0 else 0

            value = (x1+x2+carry) % 2
            carry = (x1+ x2+carry) // 2


            res.append(value)

            p1 -= 1
            p2 -= 1

        if carry != 0:
            res.append(carry)

        return "".join(str(x) for x in res[::-1])