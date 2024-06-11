from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for e in s:
            if e == "(" or e == "[" or e == "{":
                stack.append(e)
            else:
                if len(stack) == 0:
                    return False
                temp = stack.pop()
                if e == ")" and temp != "(":
                    return False
                if e == "}" and temp != "{":
                    return False
                if e == "]" and temp !="[":
                    return False
                
        if len(stack) == 0:
            return True
        else:
            return False