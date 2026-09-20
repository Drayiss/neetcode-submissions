from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = Counter(s1)

        n = len(s2)
        for i in range(n - len(s1) + 1):
            substr = s2[i : i + len(s1)]
            count_substr = Counter(substr)
            if count_s1 == count_substr:
                return True
        
        return False