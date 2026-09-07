from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        counter1 = Counter(s1)
        counter2 = Counter()
        tmp = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            counter2[s2[r]] += 1
            # when the current length is greater than s1 time to shrink
            if (r - l + 1) > len(s1):
                counter2[s2[l]] -= 1
                # when shrinking if the freq of a character is 0 remove from the map
                if counter2[s2[l]] == 0:
                    del counter2[s2[l]]
                l += 1
            if len(counter1) == len(counter2) and counter1 == counter2:
                return True
        return False
