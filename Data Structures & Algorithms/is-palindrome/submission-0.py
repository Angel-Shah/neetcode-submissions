class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left < right:
            if not self.is_alpha(s[left]):
                left += 1
                continue
            if not self.is_alpha(s[right]):
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    def is_alpha(self, c: str) -> bool:
        c = c.lower()
        if ord(c) >= 97 and ord(c) <= 122:
            return True
        if ord(c) >= 48 and ord(c) <= 57:
            return True
        return False
