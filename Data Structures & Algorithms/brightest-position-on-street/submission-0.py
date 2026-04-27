class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        diff = defaultdict(int)
        for p, r in lights:
            start, end = p-r, p+r
            diff[start] += 1
            # why? 
            diff[end+1] -= 1
        print(f"{diff=}")
        max_bright = curr = 0
        res = 0
        for key in sorted(diff):
            curr += diff[key]
            if curr > max_bright:
                max_bright = curr
                res = key
        return res