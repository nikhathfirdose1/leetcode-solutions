class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hm_s = {}
        hm_t = {}

        for c in s:
            hm_s[c] = hm_s.get(c,0) + 1

        for c in t:
            hm_t[c] = hm_t.get(c,0) + 1

        for key in hm_s:
            if key in hm_t:
                if hm_s[key] != hm_t[key]:
                    return False
            else:
                return False

        return True
        