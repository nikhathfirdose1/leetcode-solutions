class Solution:
    def minWindow(self, s: str, t: str) -> str:


        if t == "" or len(t) > len(s):
            return ""

        havemap = {}
        needmap = {}

        

        for i in t:
            needmap[i] = needmap.get(i,0) + 1

        have = 0
        need = len(needmap)

        res = [-1,-1]
        resLen = float('inf')

        l = 0


        for r in range(len(s)):

            c = s[r]
            havemap[c] = havemap.get(c,0) + 1

            
            if c in needmap and havemap[c] == needmap[c]:
                print(c)
                have += 1

            # print(f"havemap:{havemap}, have: {have}, need: {need}")
            # print("need target =", need, "distinct needed =", len(needmap), "needmap:", needmap)

            while have == need:
                # print(f"VALID window -> [{l},{r}] = '{s[l:r+1]}'")

                if (r - l + 1) < resLen:
                    res = [l,r]
                    resLen = r - l + 1

                havemap[s[l]] -= 1

                if s[l] in needmap and havemap[s[l]] < needmap[s[l]]:
                    have -= 1

                l += 1

        l, r = res
            
        return s[l:r+1] 
                    

