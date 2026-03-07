class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        unique = set()

        left = 0

        max_length = 0


        for right in range(len(s)):

            while s[right] in unique:

                print(s[left], s[right])
                unique.remove(s[left])

                left += 1

            
            unique.add(s[right])

            max_length = max(max_length, right - left +1)

            # print(unique)

        return max_length



        

# [pwwkew]

# l = 2, r= 2 ; unique = [] ; max_len = 2
