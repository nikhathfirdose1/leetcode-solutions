class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:

        s = len(sequence)
        w = len(word)

        if w > s or word not in sequence:
            return 0

        ans = 0
        i = 0

        while i <= s - w:

            if sequence[i] != word[0]:
                i += 1
                continue


            run = 0
            j = i

            while j+w <= s and sequence[j:j+w] == word:
                run += 1
                j += w

            ans = max(ans,run)
            i += 1

        return ans
            

