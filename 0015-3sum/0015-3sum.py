class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    
        ans = set()
        nums.sort()

        out = 0
        in_ = 0

        

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            if nums[i] > 0:
                break
            n2 = nums[i]
            seen = set()
            out += 1

            for j in range(i+1, len(nums)):
                n3 = nums[j]
                n1 = -n2 -n3
                in_ += 1

                if n1 in seen:
                    triplet = tuple(((n1,n2,n3)))
                    ans.add(triplet)

                seen.add(n3)

        print(out,in_)

        return [list(t) for t in ans]



