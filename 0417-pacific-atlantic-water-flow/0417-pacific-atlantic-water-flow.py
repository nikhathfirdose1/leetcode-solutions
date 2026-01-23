class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:


        if not heights or not heights[0]:
            return []

        rows = len(heights)
        cols = len(heights[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)] 

        pacific = set()
        atlantic = set()

        # visited = set()

        def dfs(r,c, visited):

            visited.add((r,c))

            for dr, dc in directions:
                nr, nc = r+dr, c+dc

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or (nr, nc) in visited:
                    continue

                if heights[nr][nc] < heights[r][c]:
                    continue
                
                dfs(nr,nc, visited)
        

        for r in range(rows):
            dfs(r, 0, pacific)
        for c in range(cols):
            dfs(0,c, pacific)

        
        for r in range(rows):
            dfs(r, cols-1, atlantic)
        for c in range(cols):
            dfs(rows-1, c, atlantic)

        return [[r,c] for (r,c) in (pacific & atlantic)]




