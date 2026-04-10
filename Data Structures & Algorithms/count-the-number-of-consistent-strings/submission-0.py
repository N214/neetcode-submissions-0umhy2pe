class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for w in words:
            print(f"{w=}")
            if all(char in allowed for char in w):
                count+=1
        return count