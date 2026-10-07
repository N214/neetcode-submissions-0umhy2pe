class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        curr = ""
        # uses / as the signal to process curr.
        for p in path + "/":
            print(p)
            if p == '/':
                if curr == "..":
                    if stack: stack.pop()
                elif curr != "" and curr != ".":
                    stack.append(curr)
                curr = ""
            else:
                curr += p
        return "/" + "/".join(stack)