from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        index_dq = deque()
        res = []

        l = 0
        for r, right_num in enumerate(nums):
            while index_dq and nums[index_dq[-1]] < right_num:
                index_dq.pop()
            index_dq.append(r)

            # Ensure correct window size
            if r - l + 1 > k:
                l += 1
                if index_dq[0] < l:
                    index_dq.popleft()

            # Add to res only if correct window size
            if r - l + 1 == k:
                res.append(nums[index_dq[0]])

        return res