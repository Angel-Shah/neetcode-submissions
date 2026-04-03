class Solution:

    def represents_int(self,s):
        try: 
            int(s)
        except ValueError:
            return False
        else:
            return True

    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for t in tokens:
            if self.represents_int(t):
                nums.append(int(t))
            if t == '+':
                nums.append(nums.pop(-2)+nums.pop(-1))
            
            if t == '-':
                nums.append(nums.pop(-2)-nums.pop(-1))
            
            if t == '*':
                nums.append(nums.pop(-2)*nums.pop(-1))

            if t == '/':
                nums.append(int(nums.pop(-2)/nums.pop(-1)))
        return int(nums[0])