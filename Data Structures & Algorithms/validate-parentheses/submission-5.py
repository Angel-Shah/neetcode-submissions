class Solution:
    def isValid(self, s: str) -> bool:
        closers = {'}':'{',')':'(',']':'['}
        stack = []
        for c in s:
            if c in closers:
                if stack and stack[-1] == closers[c]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(c)
            
        return len(stack) == 0
        
                    