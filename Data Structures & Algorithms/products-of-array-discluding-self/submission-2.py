class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        # [1,1,1,1]
        # [1,2,4,6]
        # in place prefix
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]
        #print(f"{res=}")
        
        # Backward pass: multiply by product of all elements after i
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            #print(f"{i=} {res[i]=}")
            postfix *= nums[i]
        return res