class Solution:
    def reverseParentheses(self, s: str) -> str:
        pairs = [0] * len(s)
        stack = []
        for i, c in enumerate(s):
            if c == "(":
                # append the index of open (
                stack.append(i)
            elif c == ")":
                j = stack.pop()
                pairs[i], pairs[j] = j, i
        # ex: [4, 0, 0, 0, 0]
        ans = []
        i, direction = 0, 1
        while i < len(s):
            if s[i] in "()":
                i = pairs[i]
                direction *= -1
            else:
                ans.append(s[i])
            i += direction
        return "".join(ans)
