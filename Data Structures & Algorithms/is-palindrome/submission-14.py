class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            lower_left = s[l].lower()
            lower_right = s[r].lower()
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif lower_left != lower_right:
                return False
            else:
                l += 1
                r -= 1
        
        return True