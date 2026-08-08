class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)
        while l <= r:
            m = (l + r) // 2
            hours = 0
            for p in piles:
                # for each pile, calculate the time needed to finish
                hours += math.ceil(p/m)
            if hours <= h:
                res = min(res, m)
                # mid speed is not enough, we did not consume all our time, go for a lower speed
                r = m - 1
            else:
                l = m + 1
        return res