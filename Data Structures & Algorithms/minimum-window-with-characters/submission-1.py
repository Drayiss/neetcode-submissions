from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        count_t = Counter(t)
        window = defaultdict(int)
        have, need = 0, len(count_t)
        res_indices, res_len = [-1, -1], float("inf")

        left = 0
        for right, c in enumerate(s):
            window[c] += 1
            if window[c] == count_t[c]:
                have += 1

            while have == need:
                window_len = right - left + 1
                if window_len < res_len:
                    res_indices = [left, right]
                    res_len = window_len
                
                # Remove left character from window
                left_c = s[left]
                window[left_c] -= 1
                if window[left_c] < count_t[left_c]:
                    have -= 1
                left += 1
        
        if res_len != float("inf"):
            l, r = res_indices
            return s[l : r + 1]

        return ""
        
                