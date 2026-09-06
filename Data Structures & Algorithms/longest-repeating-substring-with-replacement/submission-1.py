class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        # use a hashmap to counter the frequency in the current window
        counter = defaultdict(int)
        l = 0
        for r in range(len(s)):
            # add current values frequency
            counter[s[r]] += 1
            # if the difference between current window length
            # and the most frequent val is above k, then the window is not valid therefore to slide l  
            # (r - l + 1) length of the current window
            if (r - l + 1) - max(counter.values()) > k:
                counter[s[l]] -= 1
                l += 1
            res = max(res, r-l + 1)
        return res