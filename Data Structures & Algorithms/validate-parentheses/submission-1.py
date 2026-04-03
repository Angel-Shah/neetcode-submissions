class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'}':'{',')':'(',']':'['}
        openers = {'{','(','['}
        stack = []
        for c in s:
            if c in openers:
                stack.append(c)
            elif stack and stack[-1] != brackets[c]:
                return False
            else:
                if stack:
                    stack.pop(-1)
                else:
                    return False
        return len(stack) == 0
        
                    