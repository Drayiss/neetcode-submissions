class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_pal_index = 0
        longest_pal_length = 1

        for i in range(len(s)):
            # First expand odd substrings out
            l, r = i - 1, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_pal_length = r - l + 1
                if curr_pal_length > longest_pal_length:
                    longest_pal_index = l
                    longest_pal_length = curr_pal_length
                l -= 1
                r += 1

            # Next check even palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_pal_length = r - l + 1
                if curr_pal_length > longest_pal_length:
                    longest_pal_index = l
                    longest_pal_length = curr_pal_length
                l -= 1
                r += 1
            
        return s[longest_pal_index : longest_pal_index + longest_pal_length]
