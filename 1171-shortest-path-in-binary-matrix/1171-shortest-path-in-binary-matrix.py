class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        n = len(grid)

        if n == 1:
            if grid[0][0] == 0:
                return 1

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        
        queue = deque([(0,0,1)])
        visited = set()

        while queue:

            row, col, dist  = queue.popleft()

            visited.add((row,col))

            if row == n-1 and col == n-1:
                return dist

            directions = [(1,0), (0,1), (-1,0), (0,-1), (-1,-1), (1,1), (1,-1), (-1,1)]

            for dr, dc in directions:
                nr, nc = row + dr, col +dc

                if 0 <= nr < n and 0 <= nc < n and (nr,nc) not in visited:

                    if grid[nr][nc] == 0:
                        queue.append((nr,nc, dist+1))
                        visited.add((nr,nc))
                    

        return -1




        