class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while stack and stack[-1] > n and k > 0:
                stack.pop()
                k -= 1
            stack.append(n)
        # if the list was already stricly increasing just remove len k in the stack
        stack = stack[:len(stack)- k] if k > 0 else stack
        res = "".join(stack).lstrip("0")
        return res if res else "0"