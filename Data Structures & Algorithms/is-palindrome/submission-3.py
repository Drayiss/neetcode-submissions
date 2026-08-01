class Solution:
    def isPalindrome(self, s: str) -> bool:
        # new_str = ""

        # for c in s:
        #     if c.isalnum():
        #         new_str += c.lower()

        # return new_str == new_str[::-1]
        
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.is_alpha_numeric(s[l]):
                l += 1
            while r > l and not self.is_alpha_numeric(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def is_alpha_numeric(self, c: str) -> bool:
        return ((ord('a') <= ord(c) <= ord('z')) or
                (ord('A') <= ord(c) <= ord('Z')) or
                (ord('0') <= ord(c) <= ord('9')))