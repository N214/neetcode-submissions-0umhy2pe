class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        
        def possible(capacity):
            numOfDays, load = 1, 0
            for num in weights:
                if load + num > capacity:
                    numOfDays += 1
                    load = num
                else:
                    load += num
            return numOfDays <= days
        while l <= r:
            mid = (l + r) //2
            if possible(mid):
                r = mid -1
            else:
                l = mid +1
                
        return l