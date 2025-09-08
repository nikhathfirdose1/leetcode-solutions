class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        n = len(grid)

        parent = [i for i in range(n*n)]
        size = [1] * (n*n)


        def find(x):
            if parent[x] == x:
                return x
            
            parent[x] = find(parent[x])
            return parent[x]


        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX == rootY:
                return

            if rootX != rootY:
                if size[rootX] > size[rootY]:
                    parent[rootY] = rootX
                    size[rootX] += size[rootY]
                else:
                    parent[rootX] = rootY
                    size[rootY] += size[rootX]

                
        rows = len(grid)
        cols = len(grid[0])
        max_island = 0
        all_ones = True
        unique_roots = set()

        rd = [1,-1,0,0]
        cd = [0,0,1,-1]


        for curr_row in range(rows):
            for curr_col in range(cols):
                if grid[curr_row][curr_col] == 1:

                    ID = (cols * curr_row) + curr_col

                    for d in range(4):
                        nr = curr_row + rd[d]
                        nc = curr_col + cd[d]

                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            neigh_ID = (cols * nr) + nc
                            union(ID, neigh_ID)

        
        for curr_row in range(rows):
            for curr_col in range(cols):
                if grid[curr_row][curr_col] == 0:
                    all_ones = False

                    island = 1

                    for d in range(4):
                        nr = curr_row + rd[d]
                        nc = curr_col + cd[d]

                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            neigh = (cols * nr) + nc
                            main_root = find(neigh)
                            unique_roots.add(main_root)

                    
                    for rt in unique_roots:
                        island += size[rt]

                    unique_roots.clear()

                    max_island = max(max_island, island)



        if all_ones:
            return rows*cols

        else:
            return max_island



        