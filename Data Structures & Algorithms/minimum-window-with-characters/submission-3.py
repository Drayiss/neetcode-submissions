from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        count_t = Counter(t)
        count_window = defaultdict(int)
        have, need = 0, len(count_t)
        res_indices, res_len = [-1, -1], float("inf")

        left = 0
        for right, c in enumerate(s):
            count_window[c] += 1
            if count_t[c] == count_window[c]:
                have += 1

            while have == need:
                # Update res
                window_len = right - left + 1
                if window_len < res_len:
                    res_indices = [left, right]
                    res_len = window_len

                # Remove left character from window
                left_c = s[left]
                count_window[left_c] -= 1
                if count_window[left_c] < count_t[left_c]:
                    have -= 1
                left += 1

        if res_len < float("inf"):
            l, r = res_indices
            return s[l : r + 1]
        
        return ""

