class Solution:
    def findMin(self, nums: List[int]) -> int:

        # Idea :
        # Simple Binary Search
        # L on the left R on the right
        # mid = ( L + R ) // 2
        # if arr[mid] < arr[R], from mid to R is sorted
        # so just put R in mid since It is sorted, the leftmost part is the minimum so far
        # if arr[mid] > L from L to mid is sorted, if it is not sorted, and i want the minimum 
        # L is not the minimum, mid is not the minmum since arr[mid] > L, let's go to the next index

        if not nums:
            return 
       
        L = 0
        R = len(nums) - 1

        while L < R :
            mid = ( L + R ) // 2

            if nums[mid] < nums[R]:
                R = mid
            else :
                L = mid + 1         

  
        return nums[L]