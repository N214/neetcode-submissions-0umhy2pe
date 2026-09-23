class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = len(nums)//3
        freqCount = defaultdict(int)
        # since we have to count multiple number, this cannot be hold in one value, it has to be a hashmap
        # for this prob we will keep a small hashmap of max 2 elements
        # once we see the third, we have to check our hashmap, if the count of the element is 1 then we delete it else we just decrement its count
        # at the end, we will have at the end of nums element in the hash map that are potential candidate to the n/3 threshold, so we iterate again from the hashmap this time, if it's bigger than n/3, we add it to res. 

        for num in nums:
            freqCount[num] += 1
            if len(freqCount) <= 2:
                continue
            
            new_count = defaultdict(int)
            for k, v in freqCount.items():
                if v > 1:
                    # if the count is 1, we are deleting to inverse we only add count > 1 to the new hashmap
                    new_count[k] += v - 1
            freqCount = new_count
        res = []
        for i in freqCount:
            if nums.count(i) > freq:
                res.append(i)
            
        return res