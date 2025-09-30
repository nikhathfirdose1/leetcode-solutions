class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hm = defaultdict(list)
        ans = []

        for word in strs:
            count = [0] * 26

            for letter in word:
                count[ord(letter) - ord("a")] += 1

            hm[tuple(count)].append(word)

        for k, v in hm.items():
            ans.append(v)

        print(hm)

        return ans
        