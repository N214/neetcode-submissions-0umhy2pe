class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)
        while l <= r:
            # l, r and mid all represent the speed
            mid = (l+r)//2
            hours = 0
            for p in piles:
                # banana / (banana/hour) = hour
                hours += math.ceil(p/mid)
            # If hours <= h, then mid is fast enough, so try a smaller speed
            if hours <= h:
                res = min(res, mid)
                r = mid -1
            # speed is not enough and we exhausted all possibilities
            else:
                l = mid +1
        return res