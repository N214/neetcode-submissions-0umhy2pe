class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l,r = j+1, n - 1 # why is this n-1?
                while l < r:
                    summ = nums[i] + nums[j] + nums[l] + nums[r]
                    if summ > target:
                        # if current sum to bigger than target we take a smaller right num, since it's sorted.
                        r -= 1
                    elif summ < target:
                        # we take take a bigger left number since it's sorted
                        l += 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        r -=1
                        l +=1
                        # Explain better here, why do we do check the check after appending one element to res
                        while l < r and nums[l] == nums[l-1]:
                            l +=1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
        return res
