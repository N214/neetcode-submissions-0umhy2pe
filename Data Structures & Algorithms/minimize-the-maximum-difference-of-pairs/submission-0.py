class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0: return 0
        nums.sort()
        l, r = 0, 10**9
        res = 10**9
        def isValid(threshold):
            i, cnt = 0, 0
            while i < len(nums) -1:
                if abs(nums[i] - nums[i+1]) <= threshold:
                    cnt +=1
                    i += 2
                else:
                    i += 1
                if cnt == p:
                    return True
            return False

        while l < r:
            m = (l + r) // 2
            if isValid(m):
                res = m
                # move to left to find a even smaller one if possible
                r = m
            else:
                # otherwise move to the larger value
                l = m + 1
        return res
