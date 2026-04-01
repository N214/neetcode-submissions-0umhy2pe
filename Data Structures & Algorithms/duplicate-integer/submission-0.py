class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        data = set()
        for num in nums:
            if num in data:
                return True
            data.add(num)
        return False