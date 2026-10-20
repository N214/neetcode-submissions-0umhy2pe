class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []
        # "T?2:3"
        for e in expression[::-1]:
           # "3:2?T"
           # [3, :, 2, ?]
            if stack and stack[-1] == "?":
                # pop the t
                stack.pop()
                onTrue = stack.pop()
                # pop the :
                stack.pop()
                onFalse = stack.pop()
                if e == "T":
                    stack.append(onTrue)
                else:
                    stack.append(onFalse)
            else:
                stack.append(e)
        return stack[0]

