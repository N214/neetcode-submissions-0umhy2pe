class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        counter = defaultdict(int)
        l = 0
        for r in range(len(s)):
            counter[s[r]] += 1
            # lenghth of the window
            if (r - l + 1) - max(counter.values()) > k:
                counter[s[l]] -= 1
                l += 1
            res = max(res, r-l + 1)
        return res