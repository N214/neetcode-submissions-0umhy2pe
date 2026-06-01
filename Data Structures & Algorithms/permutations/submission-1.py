class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        perms = self.permute(nums[1:])
        res = []
        for p in perms:
            # insert at index i (at each position of the array) the val nums[0] 
            for i in range(len(p) +1):
                p_copy = p.copy()
                print(f"for {p=} insert {nums[0]} at position {i=}")
                p_copy.insert(i, nums[0])
                #print(f"sub array to append {p_copy=}")
                res.append(p_copy)
        return res