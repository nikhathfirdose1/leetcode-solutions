class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        adj = [[] for i in range(numCourses)]

        for u, v in prerequisites:
            adj[u].append(v)

        

        queue = deque([])

        in_deg = [0]* numCourses
        order = []

        for pre in prerequisites:
            a = pre[0]
            b = pre[1]

            in_deg[b] += 1

            

        for i in range(numCourses):
            if in_deg[i] == 0:
                queue.append(i)
        
        while queue:

            node = queue.popleft()
            order.append(node)

            for neigh in adj[node]:
                in_deg[neigh] -= 1

                if in_deg[neigh] == 0:
                    queue.append(neigh)


        # print(order)

        
        return len(order) == numCourses


        