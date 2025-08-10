class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        if len(heights) == 1:
            return [0]


        ans = [len(heights)-1]
        large = heights[len(heights)-1]

        for i in range(len(heights)-2, -1, -1):

            if heights[i] > large:
                ans.append(i)
                large = heights[i]

        return ans[::-1]




                
            
        