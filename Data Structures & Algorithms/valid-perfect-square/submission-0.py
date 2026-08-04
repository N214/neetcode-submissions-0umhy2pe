class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num
        while l <= r:
            m = (l+r)//2
            sqrt = m * m
            if sqrt == num:
                return True
            elif sqrt < num:
                l = m + 1
            else:
                r = m - 1
        return False