class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        ans = [len(heights)-1]
        large = heights[len(heights)-1]

        for i in range(len(heights)-1, -1, -1):

            if heights[i-1] > large:
                ans.append(i-1)
                large = heights[i-1]

        return ans[::-1]




                
            
        