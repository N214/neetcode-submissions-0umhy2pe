class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set("aeiou")
        prefix_count = [0] * (len(words) + 1)
        preSum = 0
        for i, w in enumerate(words):
            if w[0] in vowels and w[-1] in vowels:
                preSum += 1
            prefix_count[i + 1] = preSum
        res = [0] * len(queries)
        for i, q in enumerate(queries):
            l, r = q
            res[i] = prefix_count[r+1] - prefix_count[l]
        return res