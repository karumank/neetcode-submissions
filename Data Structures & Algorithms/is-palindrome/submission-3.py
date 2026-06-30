class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if  not s[left].isalnum():
                while left < len(s) - 1 and not s[left].isalnum():
                    left += 1
            if  not s[right].isalnum():
                while right >= 0 and not s[right].isalnum():
                    right -= 1
            
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True
            