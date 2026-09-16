class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s, count_t = {}, {}

        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]

            if s_char not in count_s:
                count_s[s_char] = 0
            if t_char not in count_t:
                count_t[t_char] = 0
            count_s[s_char] += 1
            count_t[t_char] += 1
        
        return count_s == count_t