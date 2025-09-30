class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hm = defaultdict(list)
        ans = []

        for word in strs:
            key = tuple(sorted(word))
            hm[key].append(word)

        for k, v in hm.items():
            ans.append(v)

        return ans
        