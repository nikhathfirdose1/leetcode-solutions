class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dist = []
        n = len(points)
        
        for point in points:
            dist.append(math.sqrt((point[0]**2) + (point[1]**2)))

        low = 0.0
        high = max(dist)

        rem = list(range(n))
        chosen = []

        if k == n:
            return points

        while len(chosen) < k and high - low > 1e-9 and rem:

            need = k - len(chosen)

            if len(rem) == need:
                chosen.extend(rem)
                break

            mid = (low+high) / 2.0

            close = [i for i in rem if dist[i] <= mid]
            far = [i for i in rem if dist[i] > mid]

            if len(close) < need:

                chosen.extend(close)
                rem = far
                low = mid

            else:

                rem = close
                high = mid

        need = k - len(chosen)

        if need >0:
            chosen.extend(rem[:need])

        return [points[i] for i in chosen]





        