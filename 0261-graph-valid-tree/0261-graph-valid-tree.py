class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        parent = [i for i in range(n)]
        rank = [1] * n

        def find(x):
            if x == parent[x]:
                return x

            parent[x] = find(parent[x])
            return parent[x]

        
        def union(x,y):
            parentx = find(x)
            parenty = find(y)

            if rank[parentx] > rank[parenty]:
                parent[parenty] = parentx

            elif rank[parentx] < rank[parenty]:
                parent[parentx] = parenty

            else:
                parent[parenty] = parentx
                rank[parentx] += 1


        # if len(edges) != n-1:
        #     return False


        for (u,v) in edges:
            if find(u) == find(v):
                return False
            
            union(u,v)

        return len(edges) == n-1

        