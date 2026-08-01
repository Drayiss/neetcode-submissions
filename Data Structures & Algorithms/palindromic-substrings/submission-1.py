class Solution:
    def countSubstrings(self, s: str) -> int:
        total_pals = 0

        for i in range(len(s)):
            total_pals += self.count_pals(s, i, i)
            total_pals += self.count_pals(s, i, i + 1)
            
        return total_pals
    
    def count_pals(self, s: str, l: int, r: int) -> int:
        total_pals = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            # We are currently in a palindrome
            total_pals += 1
            l -= 1
            r += 1
        return total_pals