class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1
        while l <=r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            # left sorted portion
            # we will consider left everything where l<mid
            if nums[l] <= nums[mid]:
                # search right if target is bigger than mid
                # search right again if target is smaller than the left most number
                
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                # else target is greater than nums[l] but less than nums[mid] then we go right
                else:
                    r = mid - 1
            
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    # go left
                    r = mid - 1
                else:
                    l = mid + 1
        return -1