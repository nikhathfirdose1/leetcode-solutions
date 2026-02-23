import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        if n == 1:
            return 0

        
        def dj(src):

            adj = {i: [] for i in range(1,n+1)}

            for u,v, w in times:
                adj[u].append((v,w))

            time = [float("inf")] * (n+1)
            time[src] = 0

            heap = []
            heapq.heappush(heap, (0, src))

            while heap:

                t, node = heapq.heappop(heap)

            
                if t != time[node]:
                    continue

                for (v, w) in adj[node]:

                    new_t = t + w
                    if new_t < time[v]:
                        time[v] = new_t
                        heapq.heappush(heap, (new_t, v))


            max_time = max(time[1:])


            return max_time if max_time < float("inf") else -1


        return dj(k)


        