class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        return num[::-1] == num
