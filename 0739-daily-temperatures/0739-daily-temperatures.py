class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        res = [0] * len(temperatures)

        for curr in range(len(temperatures)):

            while stack and  temperatures[curr] > temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = curr - prev


            stack.append(curr)

        return res
        