class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        curr_set = set()
        res = 0

        for c in s:
            while c in curr_set:
                curr_set.remove(s[l])
                l += 1
            curr_set.add(c)
            res = max(len(curr_set), res)

        return res