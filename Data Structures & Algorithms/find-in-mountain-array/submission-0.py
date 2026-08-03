class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        # find the peak
        l, r = 0, length - 1
        #l, r = 1, length - 2

        while l <= r:
            m = l + (r-l) //2
            left, mid, right = mountainArr.get(m -1), mountainArr.get(m), mountainArr.get(m+1)
            if left < mid < right:
                l = m+1
            elif left > mid > right:
                r = m-1
            else:
                break

        peak = m
        # search left portion
        l, r = 0, peak
        while l <= r:
            m = l + (r-l) //2
            val = mountainArr.get(m)
            if val == target:
                return m
            elif val < target:
                l = m + 1
            else:
                r = m - 1

        l, r = peak, length - 1
        while l <= r:
            m = l + (r-l) //2
            val = mountainArr.get(m)
            if val == target:
                return m
            elif val > target:
                l = m + 1
            else:
                r = m - 1
        return -1
