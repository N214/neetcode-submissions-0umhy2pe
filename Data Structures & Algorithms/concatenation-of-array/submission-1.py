class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for _ in range(2):
            for i in nums:
                ans.append(i)
        print(f"{ans=}")
        return ans