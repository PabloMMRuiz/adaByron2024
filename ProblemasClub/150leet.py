from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for e in tokens:
            if e == "+":
                right = stack.pop()
                left = stack.pop()
                stack.append(right+left)
            elif e == "-":
                right = stack.pop()
                left = stack.pop()
                stack.append(left-right)
            elif e == "*":
                right = stack.pop()
                left = stack.pop()
                stack.append(right*left)
            elif e == "/":
                right = stack.pop()
                left = stack.pop()
                stack.append(int(left/right))
            else:
                stack.append(int(e))
        return stack.pop()
            
                        