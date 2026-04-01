class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        output = []
        q = deque() # index
        l = r = 0
        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            # after removing the smaller values append the right pointer
            q.append(r)
            # remove left val from window
            if l > q[0]:
                q.popleft()
            # check windows is at lest seize k
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output