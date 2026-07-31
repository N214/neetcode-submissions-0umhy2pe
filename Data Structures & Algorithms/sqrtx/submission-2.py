"""
Instead of searching for the number itself,
you search for the number mid such that:
mid * mid <= x
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        ans = 0
        while l<=r:
            mid = (l + r) // 2
            #print(f"mid is {mid}")
            if (mid * mid) <= x:
                # we take also the case when mid^2 = x
                ans = mid                 
                l = mid + 1
            else:
                r = mid -1
        return ans