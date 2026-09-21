from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        index_candidates = deque()
        res = []
        
        l = 0
        for r, right_num in enumerate(nums):
            while index_candidates and right_num > nums[index_candidates[-1]]:
                index_candidates.pop()
            index_candidates.append(r)

            # Ensure correct window size
            while r - l + 1 > k:
                l += 1
                if index_candidates[0] < l:
                    index_candidates.popleft()

            # Append to res only if window is correct size
            if r - l + 1 == k:
                res.append(nums[index_candidates[0]])

        return res