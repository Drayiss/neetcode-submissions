class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_substring = s[0]

        for i in range(len(s)):
            # Check odd substrings
            l, r = i - 1, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(longest_substring):
                    longest_substring = s[l : r + 1]
                l -= 1
                r += 1

            # Check even substrings
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(longest_substring):
                    longest_substring = s[l : r + 1]
                l -= 1
                r += 1
            
        return longest_substring
        