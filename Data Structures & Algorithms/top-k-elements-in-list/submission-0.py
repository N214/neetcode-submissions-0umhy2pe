class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # res = defaultdict(int)
        # for num in nums:
        #     res[num] += 1
        # print(f"{res=}")
        # for num, _ in Counter(nums)
        return [num for num, _ in Counter(nums).most_common(k)]