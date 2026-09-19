class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curr = 0
        prefixSum = defaultdict(int)
        prefixSum[0] = 1
        for num in nums:
            curr += num
            diff = curr - k
            res += prefixSum.get(diff, 0)
            #prefixSum[curr] = 1 + prefixSum.get(curr, 0)
            prefixSum[curr] += 1
        return res