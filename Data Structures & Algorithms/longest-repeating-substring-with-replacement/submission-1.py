class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding window using counts
        longest = 0
        counts = [0] * 26
        l = 0
        n = len(s)

        for r in range(n):
            r_value = ord(s[r]) - ord("A")
            counts[r_value] += 1
            # While there are more than k characters to replace
            while (r - l + 1) - max(counts) > k:
                l_value = ord(s[l]) - ord("A")
                counts[l_value] -= 1
                l += 1
            new_window_length = r - l + 1
            longest = max(longest, new_window_length)
        
        return longest

