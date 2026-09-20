class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        count_s = Counter(s)
        count_t = Counter(t)

        for key in count_s.keys():
            if count_s[key] != count_t[key]:
                return False
        
        return True