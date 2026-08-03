class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        ans = 0
        while l <= r:
            m = (l + r)//2
            sqrt = m * m
            if sqrt == x: 
                return m
            elif sqrt > x:
                r = m -1
            else:
                ans = m
                l = m+1
        return ans