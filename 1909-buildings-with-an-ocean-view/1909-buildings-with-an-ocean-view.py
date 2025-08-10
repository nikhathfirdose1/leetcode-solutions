class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        ans = [len(heights)-1]
        large = heights[len(heights)-1]

        for i in range(len(heights)-2, -1, -1):

            if heights[i] > large:
                ans.append(i)
                large = heights[i]

        return ans[::-1]




                
            
        