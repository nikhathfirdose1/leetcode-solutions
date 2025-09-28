class Solution:
    def addBinary(self, a: str, b: str) -> str:

        carry = 0
        res = 0

        p1 = len(a) - 1
        p2 = len(b) - 1

        res = []

        while p1 >= 0 or p2 >= 0:

            x1 = int(a[p1]) if p1>= 0 else 0
            x2 = int(b[p2]) if p2 >= 0 else 0

            value = (x1+x2+carry) % 2
            carry = (x1+ x2+carry) // 2


            res.append(value)

            p1 -= 1
            p2 -= 1

        if carry != 0:
            res.append(carry)

        return "".join(str(x) for x in res[::-1])