class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res will hold the final results. Start with 1s since we'll multiply into them.
        res = [1] * len(nums)

        # FIRST PASS: compute prefix products
        # prefix is the product of all elements to the left of the current index
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix       # store left-side product for index i
            prefix *= nums[i]     # update prefix to include nums[i] for the next position

        # SECOND PASS: compute postfix products and multiply into res
        # postfix is the product of all elements to the right of the current index
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix      # multiply by right-side product for index i
            postfix *= nums[i]     # update postfix to include nums[i] for the next position to the left

        # res[i] now equals the product of all nums except nums[i]
        return res