class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]):

        adj = [[] for i in range(numCourses)]
        indeg = [0] * numCourses
        queue = deque()

        for u, v in prerequisites:
            adj[u].append(v)
            indeg[v] += 1

        for i in range(numCourses):
            if indeg[i] == 0:
                queue.append(i)

        processed = 0

        while queue:
            node = queue.popleft()
            processed += 1


            for neigh in adj[node]:
                indeg[neigh] -= 1
                if indeg[neigh] == 0:
                    queue.append(neigh)

        return processed == numCourses
