class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]
        for i, t in enumerate(temperatures):
            while stack:
                if t > stack[-1][0]:
                    _, stackIdx = stack.pop()
                    res[stackIdx] = (i - stackIdx)
                else:
                    break
            stack.append([t,i])
        return res