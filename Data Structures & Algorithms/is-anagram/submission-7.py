from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for c in s:
            s_dict[c] += 1
        
        for c in t:
            t_dict[c] += 1
        
        for s_key, s_val in s_dict.items():
            if s_key not in t_dict or t_dict[s_key] != s_val:
                return False
        
        return True