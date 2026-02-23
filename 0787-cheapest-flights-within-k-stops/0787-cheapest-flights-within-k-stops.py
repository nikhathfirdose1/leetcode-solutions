class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        

        def dj(src):

            adj = {i: [] for i in range(n)}

            for u,v, w in flights:
                adj[u].append((v, w))


            max_stops = k + 1
            prices = [[float("inf")] * n for _ in range(max_stops +1)]
            prices[0][src] = 0

            
            heap = []
            heapq.heappush(heap, ((0,src,0)))

            while heap:

                p, dest, stop = heapq.heappop(heap)

                if p != prices[stop][dest]:
                    continue

                if dest == dst:
                    return p

                if stop == max_stops:
                    continue

                for (v, w) in adj[dest]:
                    new_p = p + w
                    new_stop = stop + 1
                    if new_p < prices[new_stop][v]:
                    
                        prices[new_stop][v] = new_p
                    
                        heapq.heappush(heap,((new_p), v, new_stop))

            
            return -1

        
        return dj(src)