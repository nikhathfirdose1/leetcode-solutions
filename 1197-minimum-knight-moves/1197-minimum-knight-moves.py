class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        
        visited = set()

        directions = [(1,2) , (1, -2), (-1, 2), (-1, -2), (2,1), (2,-1), (-2,-1), (-2, 1)]

        dist = 0
        queue = deque([(0,0, dist)])
        visited.add((0,0))

        a = abs(x)
        b = abs(y)

        min_r = - 2
        min_c = - 2

        max_r = a + 2
        max_c = b + 2

        while queue:

            r, c, dist = queue.popleft()




            if (r, c) == (a,b):
                return dist

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc


                if min_r <= nr <= max_r and min_c <= nc <= max_c and (nr, nc) not in visited:
                    visited.add((nr,nc))
                    queue.append((nr,nc, dist+1))
        