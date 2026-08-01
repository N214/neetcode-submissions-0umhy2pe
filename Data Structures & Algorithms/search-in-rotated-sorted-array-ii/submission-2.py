"""
Time complexity: O(logn) best case, O(n) worst case
Space complexity: 1
"""
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) -1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return True
            if nums[l] == nums[mid]:
                # shift the left pointer since we have duplicate
                l += 1
            elif nums[l] < nums[mid]: # left side
                if nums[l] <= target < nums[mid]:
                    r = mid -1 
                else:
                    l = mid + 1

            else: # right side
                if nums[mid] < target <= nums[r]:
                    l = mid +1 
                else:
                    r = mid - 1
        return False
            