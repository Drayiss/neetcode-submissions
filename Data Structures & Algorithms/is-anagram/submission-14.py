class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}
        for c in s:
            if c not in count_s:
                count_s[c] = 1
            else:
                count_s[c] += 1
        for c in t:
            if c not in count_t:
                count_t[c] = 1
            else:
                count_t[c] += 1

        for key in count_s.keys():
            if key not in count_t or count_t[key] != count_s[key]:
                return False

        return True