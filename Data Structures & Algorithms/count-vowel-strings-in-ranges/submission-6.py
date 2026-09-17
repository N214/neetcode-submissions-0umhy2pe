class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        res = []
        voels = ["a", "e", "i", "o", "u"]
        for l,r in queries:
            #print(f"{l, r}")
            count = 0
            for w in words[l:r+1]:
                if w[0] in voels and w[-1] in voels:
                    #print(w)
                    count += 1
            res.append(count)
        return res
