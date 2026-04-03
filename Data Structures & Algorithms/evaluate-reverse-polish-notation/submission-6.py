class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for t in tokens:
            if t == '+':
                nums.append(nums.pop(-2)+nums.pop(-1))
            elif t == '-':
                nums.append(nums.pop(-2)-nums.pop(-1))
            elif t == '*':
                nums.append(nums.pop(-2)*nums.pop(-1))
            elif t == '/':
                nums.append(int(nums.pop(-2)/nums.pop(-1)))
            else:
                nums.append(int(t))
        return int(nums[0])