class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    
        ans = set()
        nums.sort()

        for i in range(len(nums)):
            n2 = nums[i]
            seen = set()

            for j in range(i+1, len(nums)):
                n3 = nums[j]
                n1 = -n2 -n3

                if n1 in seen:
                    triplet = tuple(((n1,n2,n3)))
                    ans.add(triplet)

                seen.add(n3)

        return [list(t) for t in ans]



