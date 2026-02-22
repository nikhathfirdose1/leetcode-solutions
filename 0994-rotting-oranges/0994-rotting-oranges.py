class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])



        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        queue = deque()
        fresh = 0


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row,col, 0))
                elif grid[row][col] == 1:
                    fresh += 1

        if fresh == 0:
            return 0
        elif fresh > 0 and len(queue) == 0:
            return -1
        

        while queue:

            r, c, minute = queue.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc           

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr,nc, minute + 1))

        

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1
                
        return minute  
        


            


        