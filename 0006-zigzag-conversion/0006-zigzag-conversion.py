class Solution:
    def convert(self, s: str, numRows: int) -> str:

        n = len(s)

        if numRows == 1 or numRows > n:
            return s


        rows = [""] * numRows

        row = 0
        flag = False


        for char in s:


            rows[row] += char  

            if row == 0 or row == numRows - 1:
                flag = not flag

            if flag:
                row += 1
            else:
                row -= 1

        return "".join(rows)
