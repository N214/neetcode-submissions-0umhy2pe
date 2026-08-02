class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # binary search with the min possible value of res and the maximum
        l, r = max(nums), sum(nums)
        res = r

        def canSplit(largest):
            subarray = 1
            curSum = 0
            for n in nums:
                curSum += n
                if curSum > largest:
                    subarray += 1
                    curSum = n
            return subarray <= k

        while l <= r:
            mid = l + (r-l)//2
            # if we can split the array into m and have a number that is smaller than mid, we founda new minimum
            if canSplit(mid):
                # we found a smaller res
                res = mid
                r = mid -1
            else:
                l = mid + 1
        return res
        
