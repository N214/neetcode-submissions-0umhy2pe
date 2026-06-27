"""
For this problem we have several piles of bananas (piles[i]) and h is the time available to eat 
it all. 
We can say that the speed is the lenght of the highest pile and since h >= len(pile), 
we are sure to eat it all. But here we want to find the min speed to eat it all. 
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)
        while l <= r:
            mid = (l+r)//2 # speed
            hours = 0
            for p in piles:
                # banana / (banana/h) = hour
                hours += math.ceil(p/mid)
            if hours <= h:
                # mid speed is not enough, we did not consume all our time, go for a lower speed
                # so we need to move h
                res = min(res, mid)
                r = mid -1
            else:
                l = mid +1
        return res

                