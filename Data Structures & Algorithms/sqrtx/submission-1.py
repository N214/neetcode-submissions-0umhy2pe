class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        if x < 2:
            return x
        while l<=r:
            mid = (l + r) // 2
            #print(f"mid is {mid}")
            if (mid * mid) > x:
                #print(f"{mid} squared is bigger than {x}")
                r = mid -1
            #elif x - (mid * mid) > 1:
            else:
                l = mid + 1
            # else:
            #     return mid
        return r