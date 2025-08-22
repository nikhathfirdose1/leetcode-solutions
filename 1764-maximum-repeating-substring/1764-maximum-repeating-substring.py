class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:

        to_find = word
        ans = 0

        while to_find in sequence:
            to_find += word
            ans += 1

        return ans
        