class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel = set("aeiou")
        # [1, 1, 2, 3, 4]
        #  0.    2
        prefix = [0] * (len(words) + 1)
        for i, word in enumerate(words):
            currSum = 0
            #if word[0] in vowel and word[::-1] in vowel:
            if word[0] in vowel and word[-1] in vowel:
                currSum += 1
            prefix[i+1] = prefix[i] + currSum
        
        print(f"{prefix=}")
        res = [0] * len(queries)
        for i, q in enumerate(queries):
            l, r = q
            print(f"{r=}")
            print(f"{l=}")
            res[i] = prefix[r+ 1] - prefix[l]
            print(f"{res[i]=}")
        return res