class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s, count_t = {}, {}

        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]

            count_s[s_char] = count_s.get(s_char, 0) + 1
            count_t[t_char] = count_t.get(t_char, 0) + 1
        
        return count_s == count_t