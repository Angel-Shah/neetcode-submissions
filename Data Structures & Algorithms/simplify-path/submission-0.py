class Solution:
    def simplifyPath(self, path: str) -> str:

        cmds = path.split('/')
        stack = []
        for c in cmds:
            if c not in ['','.','/']:
                if c == '..':
                    if stack:
                        stack.pop()
                    continue
                stack.append(c)
        
        # print(cmds)
        # print(stack)
        result = "/"
        if not stack:
            return result
        else:
            for s in stack:
                result += s+'/'

        return result[:-1]