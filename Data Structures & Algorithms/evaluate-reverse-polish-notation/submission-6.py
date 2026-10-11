class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                res = stack.pop() + stack.pop()
                stack.append(res) 
            elif token == "-":
                num1, num2 = stack.pop(), stack.pop()
                res = num2 - num1
                stack.append(res) 
            elif token == "*":
                num1, num2 = stack.pop(), stack.pop()
                res = num2 * num1
                stack.append(res) 
            elif token == "/":
                num1, num2 = stack.pop(), stack.pop()
                res = int(num2 / num1)
                stack.append(res) 
            else:
                stack.append(int(token))
        
        return stack[-1]