class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
    
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    # pop everything before encountering [
                    # use stack.pop + substr and not substr += stack.pop() because each new element needs to be on the top
                    substr = stack.pop() + substr
                stack.pop() # pop one more time the [
                k = ""
                while stack and stack[-1].isdigit():
                    # pop all the int to construct the number
                    k = stack.pop() + k
                # add them back to the stack
                stack.append(int(k) * substr)
        return "".join(stack)