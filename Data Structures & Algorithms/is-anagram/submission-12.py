from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = Counter()
        count_t = Counter()
        for c in s:
            count_s[c] += 1
        for c in t:
            count_t[c] += 1
        
        return count_s == count_t