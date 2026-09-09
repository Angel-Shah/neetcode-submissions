class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                curr_string = ""
                while stack and stack[-1] != '[':
                    curr_string = stack.pop() + curr_string
                stack.pop()

                curr_multiplier = ""
                while stack and stack[-1].isdigit():
                    curr_multiplier = stack.pop() + curr_multiplier
                stack.append(int(curr_multiplier) * curr_string)
            
        return "".join(stack)
                