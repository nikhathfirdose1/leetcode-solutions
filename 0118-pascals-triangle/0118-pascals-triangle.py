class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        tri = []

        for r in range(numRows):
            row = []

            for c in range(r+1):
                if c== 0 or c== r:
                    row.append(1)
                else:
                    row.append(tri[r-1][c-1]+ tri[r-1][c])

            tri.append(row)
        
        return tri
        