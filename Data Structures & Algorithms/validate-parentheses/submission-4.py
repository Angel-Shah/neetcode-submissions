class Solution:
    def isValid(self, s: str) -> bool:
        closers = {'}':'{',')':'(',']':'['}
        openers = {'{','(','['}
        stack = []
        for c in s:
            if c in openers:
                stack.append(c)
            if c in closers:
                if stack and stack[-1] == closers[c]:
                    stack.pop(-1)
                else:
                    return False
        return len(stack) == 0
        
                    