class Solution:

    def encode(self, strs: List[str]) -> str:
        # for encode from a list of string to a string, we need a sparator and the number of charrater
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res 
    def decode(self, s: str) -> List[str]:
        #.  5#hello7#nicolas
        # import to have two pointer here to define the limit in the array
        res = []
        i = 0
        while i < len(s):
            j = i 
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            res.append(word)
            i = j + 1 + length
        return res






