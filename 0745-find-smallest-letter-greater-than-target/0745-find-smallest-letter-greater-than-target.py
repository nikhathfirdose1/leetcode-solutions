class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        n = len(letters) 

        left = 0 
        right = n - 1
        res = letters[0]

        while left <= right:

            mid = (left+ right) // 2

            if ord(target) < ord(letters[mid]):
                res = letters[mid]
                right = mid -1

            else:
                left = mid + 1

        return res

        