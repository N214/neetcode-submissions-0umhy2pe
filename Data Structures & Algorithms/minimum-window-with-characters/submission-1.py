class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        counter = Counter(t)
        window = defaultdict(int)
        have, need = 0, len(counter)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            window[s[r]] += 1
            if s[r] in counter and window[s[r]] == counter[s[r]]:
                have += 1
            while have == need:
                # Update the res
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in counter and window[s[l]] < counter[s[l]]:
                    have -= 1
                l += 1


        l, r = res
        if resLen != float("infinity"):
            return s[l:r+1]
        return ""

        