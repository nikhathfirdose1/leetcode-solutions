class Solution:
    def reorganizeString(self, s: str) -> str:

        hm = {}
        ans = []
        max_heap = []

        for ch in s:
            hm[ch] = hm.get(ch, 0) + 1
        
        for k,v in hm.items():
            heapq.heappush(max_heap, (-v, k))

        n = len(s)
        if max(hm.values()) > (n + 1) // 2:
            return ""

        while len(ans) < len(s):
            count_f, char_f = heapq.heappop(max_heap)
            count_f = -1 * (count_f)

            if not ans or ans[-1] != char_f:
                
                ans.append(char_f)
                count_f -= 1
                if count_f > 0:
                    heapq.heappush(max_heap, (-count_f, char_f))

            else:
                if not max_heap:
                    return ""

                count_s, char_s = heapq.heappop(max_heap)
                count_s = -1 * count_s
                ans.append(char_s)
                count_s -= 1
                if count_f > 0:
                    heapq.heappush(max_heap, (-count_s, char_s))

                heapq.heappush(max_heap, (-count_f, char_f))
            

        return "".join(ans)


            
        
            
            

        

        