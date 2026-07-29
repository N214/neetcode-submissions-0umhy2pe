class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1

        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                return nums.index(target)
            if nums[mid] > target:
                # search left
                r = mid - 1
            else:
                # search right
                l = mid + 1
        # When the while loop exits, l is the first index 
        # where nums[l] >= target, which is exactly the insertion point, so returning l (not l + 1) is correct.
        return l
