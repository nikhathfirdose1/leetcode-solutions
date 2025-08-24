class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:



        rows = len(grid)
        cols = len(grid[0])

        if grid[0][0] !=0 or grid[rows-1][cols-1] !=0:
            return -1


        queue = deque([(0,0,1)])
        visited = set()
        visited.add((0,0))

        directions = [(1,0), (0,1), (-1,0), (0,-1), (-1,-1), (-1,1), (1,-1),(1,1)]

        while queue:
            row, col, dist = queue.popleft()

            if (row, col) == (rows-1, cols -1):
                return dist

            for dr,dc in directions:
                nr, nc = row + dr, col + dc 


                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited:
                    

                    if grid[nr][nc] == 0:
                        # prin÷t(nr,nc)
                        
                        queue.append((nr,nc, dist+1))
                        visited.add((nr,nc))


        return -1

                    




        