class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = len(strs[0])
        prefix = strs[0]

        for s in strs: 
            while s[0:length] != prefix[0:length]:
                length -= 1
            
        return prefix[0:length]