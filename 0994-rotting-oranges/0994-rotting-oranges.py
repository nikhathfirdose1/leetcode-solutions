class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1,0), (0,-1), (1,0), (0,1)]

        queue = deque([])
        visited = set()
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c, count))
                    visited.add((r,c))

        while queue:

            r, c, count = queue.popleft()

            for dr, dc in directions:
                nr, nc = r+dr, c+dc

                if nr <0 or nr >= rows or nc<0 or nc >= cols or (nr,nc) in visited:
                    continue

                if grid[nr][nc] == 1:
                    visited.add((nr,nc))
                    grid[nr][nc] = 2
                    queue.append((nr,nc, count+1))
                    

        for r in range(rows):
            # for c in range(cols):
                if 1 in grid[r]:
                    return -1

        return count        


            

