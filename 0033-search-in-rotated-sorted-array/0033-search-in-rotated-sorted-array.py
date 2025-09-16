class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def bs(s,e):

            while s <=e:    
                m = (s+e) // 2

                if nums[m] == target:
                    return m

                elif target < nums[m]:
                    e = m -1
                
                else:
                    s = m + 1

            return -1 

        n = len(nums)

        left = 0
        right = n - 1

        while left <= right:

            if nums[left] <= nums[right]:            
                return bs(left, right)

            mid = (left + right) // 2
            prev = (mid + n -1) % n
            nxt = (mid +1)% n

            if nums[prev] >= nums[mid] and nums[nxt] >= nums[mid]: 
                if nums[mid] <= target <= nums[right]:
                    return bs(mid, right)
                else:
                    return bs(0, mid - 1)

            if nums[left] <= nums[mid]:
            
                if nums[left] <= target <= nums[mid]:
                    return bs(left, mid)
                
                left = mid + 1
            else:
                
                if nums[mid] <= target <= nums[right]:
                    return bs(mid, right)
                right = mid - 1


        return -1


    
        