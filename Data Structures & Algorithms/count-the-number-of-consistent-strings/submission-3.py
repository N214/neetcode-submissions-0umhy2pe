class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # bitmask solution
        bit_mask = 0
        for c in allowed:
            bit = 1 << ord(c) - ord("a")
            bit_mask = bit_mask | bit
            # 0000
            # 0001
        res = len(words)
        for w in words:
            for c in w:
                bit = 1 << ord(c) - ord("a")
                if bit & bit_mask == 0:
                    res -= 1
                    break
        return res
