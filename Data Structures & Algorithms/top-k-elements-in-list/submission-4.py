class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort algo
        count = defaultdict(int) #{let's have the dict using the num as key and default to 0, and we increment by one for each number occurance}
        freq = [[] for i in range(len(nums)+1)] # list of list, element where the occurance is the key and the value is num so that we know how many occurance happend per num

        # when both data input is read, we start from the end of freq and interate back to check the top k occurrence 
        for num in nums:
            count[num] += 1
        #print(f"{count=}")
        for n,c in count.items():
            freq[c].append(n)
        #print(f"{freq=}")
        res = []
        # len(freq) -1 because freq is len(nums) + 1. freq has length len(nums) + 1. The indices represent frequencies from 0 to len(nums).
        for i in range(len(freq) -1, 0, -1):
            print(i)
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res