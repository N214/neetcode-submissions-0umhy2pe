class Solution:
    def maxScore(self, s: str) -> int:
        zero = 0
        one = s.count("1")
        res = 0
        # we consider that we have the whole array on the right side (that's why we count the 1's) and nothing on the left side, as we iterate through we add the left side so each time we get a 0 we add it. But if it's not a 0 it's a 1, if it's a 1 our rightSide is losing a count. 
        # len(s) -1 because we dont want to add the last element portion to the left
        for i in range(len(s) -1):
            if s[i] == "0":
                zero += 1
            else:
                one -= 1
            res = max(res, zero + one)
        
        return res