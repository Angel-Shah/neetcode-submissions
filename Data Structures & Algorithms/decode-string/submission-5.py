class Solution:
    def decodeString(self, s: str) -> str:
    
        self.r = 0
        def recursion():
            curr_ans = ""
            curr_digit = 0

            while self.r < len(s):
                c = s[self.r]
                if c.isdigit():
                    curr_digit = (curr_digit * 10) + int(c)
                elif c == '[':
                    self.r += 1
                    curr_ans += (curr_digit * recursion())
                    curr_digit = 0
                elif c == ']':
                    return curr_ans
                else:
                    curr_ans += c
                self.r += 1


            return curr_ans
        return recursion()

        