class Solution:
    def countSubstrings(self, s: str) -> int:
        total_pals = 0

        for i in range(len(s)):
            # Check odd palindromic substrings
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # We are currently in a palindrome
                total_pals += 1
                l -= 1
                r += 1
            
            # Check even palindromic substrings
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # We are currently in a palindrome
                total_pals += 1
                l -= 1
                r += 1
            
        return total_pals