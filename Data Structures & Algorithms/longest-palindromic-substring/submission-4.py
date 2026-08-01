class Solution:
    def longestPalindrome(self, s: str) -> str:
        long_index = 0
        long_length = 1

        for i in range(len(s)):
            # Check odd substrings
            l, r = i - 1, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_length = r - l + 1
                if curr_length > long_length:
                    long_index = l
                    long_length = curr_length
                l -= 1
                r += 1
            
            # Check even substrings
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_length = r - l + 1
                if curr_length > long_length:
                    long_index = l
                    long_length = curr_length
                l -= 1
                r += 1
            
        return s[long_index : long_index + long_length]