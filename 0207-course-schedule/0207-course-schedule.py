class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        indegree =  [0] * numCourses
        
        adj = defaultdict(list)

        for u,v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        
        topo = []

        while queue:
            node = queue.popleft()
            topo.append(node)

            for neigh in adj[node]:
                indegree[neigh] -= 1

                if indegree[neigh] == 0:
                    queue.append(neigh)

        
        return len(topo) == numCourses
