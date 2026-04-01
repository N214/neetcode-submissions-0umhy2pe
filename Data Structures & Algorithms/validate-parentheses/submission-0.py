class Solution:
    def isValid(self, s: str) -> bool:
        data = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for c in s:
            if c in data:
                if stack and stack[-1] == data[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False