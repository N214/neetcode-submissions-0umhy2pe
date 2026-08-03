class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        res = 0
        def canComplete(m):
            total = (m/2)*(m+1)
            if total > n:
                return False
            return True
        while l <= r:
            # mid is the rows we are considering
            m = (l + r)//2
            if canComplete(m):
                l = m + 1
                res = max(m, res)
            else:
                r = m -1
        return res
            
