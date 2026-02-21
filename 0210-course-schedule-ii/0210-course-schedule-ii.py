class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        if len(prerequisites) == 0:
            return [i for i in range(numCourses)]

        
        adj = [[] for i in range(numCourses)]

        in_deg = [0] * numCourses

        for a, b in prerequisites:
            adj[b].append(a)
            in_deg[a] += 1
            

        
        queue = deque([i for i in range(numCourses) if in_deg[i] == 0])
        order = []

        while queue:

            node = queue.popleft()
            order.append(node)

            for neigh in adj[node]:
                in_deg[neigh] -= 1

                if in_deg[neigh] == 0:
                    queue.append(neigh)

        
        return order if len(order) == numCourses else []


        