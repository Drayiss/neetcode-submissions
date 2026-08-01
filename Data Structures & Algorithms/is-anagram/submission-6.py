from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False

        # count_s_dict = defaultdict(int)
        # count_t_dict = defaultdict(int)

        # for i in range(len(s)):
        #     current_s_char = s[i]
        #     current_t_char = t[i]
        #     count_s_dict[current_s_char] += 1
        #     count_t_dict[current_t_char] += 1
        
        # return count_s_dict == count_t_dict
        return Counter(s) == Counter(t)