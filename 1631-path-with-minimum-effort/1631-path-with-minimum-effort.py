class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        rows = len(heights)
        cols = len(heights[0])

        diff_matrix = [[float("inf")] * cols for _ in range(rows)]
        diff_matrix[0][0] = 0

        directions = [(1,0), (0,1), (-1,0), (0,-1)]


        heap = []
        heapq.heappush(heap, (0, 0, 0))
        

        while heap:

            effort, r, c = heapq.heappop(heap)



            if effort != diff_matrix[r][c]:
                continue

            if r == rows - 1 and c == cols -1:
                return effort


            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    new_effort = max(effort, abs(heights[r][c] - heights[nr][nc]))

                    if new_effort < diff_matrix[nr][nc]:
                        diff_matrix[nr][nc] = new_effort
                        heapq.heappush(heap, (new_effort, nr,nc))

        return -1
        