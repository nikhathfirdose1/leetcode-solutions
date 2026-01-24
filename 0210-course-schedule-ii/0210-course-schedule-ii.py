class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]):

        adj = [[] for i in range(numCourses)]
        indeg = [0] * numCourses
        queue = deque()

        for u,v in prerequisites:
            adj[u].append(v)
            indeg[v] += 1

        for i in range(numCourses):
            if indeg[i] == 0:
                queue.append(i)

        order = []
        res = []

        while queue:
            node = queue.popleft()

            order.append(node)


            for neigh in adj[node]:
                indeg[neigh] -= 1
                if indeg[neigh] == 0:
                    queue.append(neigh)
        
        if len(order) == numCourses:
            for i in range(len(order)-1, -1, -1):
                res.append(order[i])
        
        return res