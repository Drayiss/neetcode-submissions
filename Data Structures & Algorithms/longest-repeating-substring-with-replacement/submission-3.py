class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding window while tracking counts
        longest = 0
        counts = [0] * 26
        l = 0

        n = len(s)
        for r in range(n):
            # Update counts with the right character's value
            counts[ord(s[r]) - ord("A")] += 1

            # While there are more than k characters to replace
            while (r - l + 1) - max(counts) > k:
                # Decrement count for left character
                counts[ord(s[l]) - ord("A")] -= 1

                l += 1

            longest = max(longest, (r - l + 1))
        
        return longest