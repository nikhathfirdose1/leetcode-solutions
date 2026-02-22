class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        rows = len(mat)
        cols = len(mat[0])

        result = [[0] * cols for i in range(rows)]

        queue = deque()
        visited = set()

        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    queue.append((row,col, 0))
                    visited.add((row,col))
        
        while queue:

            r, c, dist = queue.popleft()
            visited.add((r,c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    queue.append((nr, nc, dist + 1))
                    result[nr][nc] = dist + 1
                    
        return result
                        



        