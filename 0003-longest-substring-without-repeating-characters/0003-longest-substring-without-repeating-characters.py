class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        longest = 0
        unique = set()
        ans = 0 

        for r in range(len(s)):
            
            while s[r] in unique:
                unique.remove(s[l])
                l += 1

            unique.add(s[r])
            ans = max(ans, ((r-l) + 1))

        print(unique)



        return ans
