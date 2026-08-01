class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_substring_index = 0
        longest_substring_length = 1

        for i in range(len(s)):
            # Check odd substrings
            l, r = i - 1, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                current_length = r - l + 1
                if current_length > longest_substring_length:
                    longest_substring_index = l
                    longest_substring_length = current_length
                l -= 1
                r += 1

            # Check even substrings
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                current_length = r - l + 1
                if current_length > longest_substring_length:
                    longest_substring_index = l
                    longest_substring_length = current_length
                l -= 1
                r += 1
            
        return s[longest_substring_index : longest_substring_index + longest_substring_length]
        