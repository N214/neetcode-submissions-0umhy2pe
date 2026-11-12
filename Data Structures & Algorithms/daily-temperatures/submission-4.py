class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #(i, t)
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                prevIndex, prevTemp = stack.pop()
                res[prevIndex] = i - prevIndex
            stack.append((i, t))
        return res