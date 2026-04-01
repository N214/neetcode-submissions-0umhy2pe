class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        data1 = defaultdict(int)
        data2 = defaultdict(int)
        for i in s:
            data1[i] += 1
        
        for i in t:
            data2[i] += 1
        if data1 == data2:
            return True
        return False