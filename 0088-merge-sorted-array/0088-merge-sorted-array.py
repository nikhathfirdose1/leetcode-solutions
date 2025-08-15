class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        """
        
        f = m - 1
        s = n - 1
        r = len(nums1) - 1
        
        while r >=0:


            if s <0 :
                break

            if nums1[f] <= nums2[s] or f <0:
                nums1[r] = nums2[s]
                s -= 1
                r -= 1
   
            else :
                nums1[r] = nums1[f]
                f -= 1
                r -= 1





