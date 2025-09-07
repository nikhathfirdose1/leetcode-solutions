class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        n = len(grid)
        root = [i for i in range(n*n)]
        rank = [1] * (n * n)
        size = [1] * (n * n)

        def find(x):
            if root[x] == x:
                return x

            root[x] = find(root[x])
            return root[x]

        def union(x,y):
            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    root[rootY] = rootX
                    size[rootX] += size[rootY]
                elif rank[rootX] < rank[rootY]:
                    root[rootX] = rootY
                    size[rootY] += size[rootX]
                else:
                    root[rootY] = rootX
                    rank[rootX] += 1
                    size[rootX] += size[rootY]

        
        rows = len(grid)
        cols = len(grid[0])

        rd = [1,-1,0,0]
        cd = [0,0,1,-1]

        for curr_row in range(rows):
            for curr_col in range(cols):

                if grid[curr_row][curr_col] == 1:
                    node = (cols * curr_row) + curr_col

                    for direction in range(4):
                        neigh_row = curr_row + rd[direction]
                        neigh_col = curr_col + cd[direction]

                        if 0 <= neigh_row < rows and 0 <= neigh_col < cols and grid[neigh_row][neigh_col] == 1:
                            neigh_node = (cols * neigh_row) + neigh_col
                            union(node, neigh_node)


        # for i in range(len(root)):
        #     if root[i] == i:
        #         print("ROOT:", i, "rank:", rank[i])

        max_island = 0 
        unique = set()
        zero = False

        for curr_row in range(rows):
            for curr_col in range(cols):
                if grid[curr_row][curr_col] == 0:
                    zero = True
                    island = 1

                    for d in range(4):
                        neigh_row = curr_row + rd[d]
                        neigh_col = curr_col + cd[d]

                        if 0 <= neigh_row < rows and 0 <= neigh_col < cols and grid[neigh_row][neigh_col] == 1:
                            neigh_node = (cols * neigh_row) + neigh_col

                            main_root = find(neigh_node)
                            unique.add(main_root)

                    for r in unique:
                        island += size[r]
                        
                    unique.clear()

                    max_island = max(max_island, island)

        if not zero:
            return rows * cols
        
        return max_island


        






        