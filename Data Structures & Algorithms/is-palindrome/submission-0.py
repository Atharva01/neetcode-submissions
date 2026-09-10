import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        left = 0
        right = len(s) - 1
        same = 0
        while left < right:
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -=1
        return True