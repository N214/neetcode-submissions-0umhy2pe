class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        for num, t in Counter(nums).most_common(k):
            print(f"{num=} and {t=}")

        return [num for num, _ in Counter(nums).most_common(k)]