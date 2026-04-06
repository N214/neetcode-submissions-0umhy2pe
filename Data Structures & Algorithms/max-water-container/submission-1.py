class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) -1
        maxVol = 0
        while left < right:
        
            vol = (right - left) * min(heights[left], heights[right])
            maxVol = max(maxVol, vol)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -=1
        return maxVol