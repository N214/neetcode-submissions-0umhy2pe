import heapq

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        res = []
        while nums:
            smallest = heapq.heappop(nums)
            res.append(smallest)
        return res