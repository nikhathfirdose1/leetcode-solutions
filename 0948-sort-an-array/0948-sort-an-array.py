class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        


        def merge_sort(arr):

            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            return merged(left, right)

        
        def merged(l,r):

            merged = []
            i,j = 0,0

            while i < len(l) and j < len(r):

                if l[i] <= r[j]:
                    merged.append(l[i])
                    i += 1

                else:
                    merged.append(r[j])
                    j += 1

            
            merged.extend(l[i:])
            merged.extend(r[j:])


            return merged

        return merge_sort(nums)