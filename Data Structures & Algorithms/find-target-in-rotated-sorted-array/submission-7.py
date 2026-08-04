# [4,5,6,7,0,1,2]
#  l     m     r 

# [4,5,6,7,0,1,2]
#          l m r 

# [4,5,6,7,0,1,2]
#          l m  
#          r     
# [4,5,6,7,0,1,2]
#          r=l=m   
#               
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r)//2
            if target == nums[m]:
                return m
            # left half is sorted
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # right half is sorted
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1