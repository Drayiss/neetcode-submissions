from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        # Monotonic decreasing dequeue
        index_dq = deque()
        l = r = 0
        n = len(nums)

        while r < n:
            # Check if new num is greater than or equal to back of queue
            while index_dq and nums[r] >= nums[index_dq[-1]]:
                index_dq.pop()
            index_dq.append(r)

            # Update window to correct size
            if l > index_dq[0]:
                index_dq.popleft()

            # Only append to output if window has reached correct size
            if (r + 1) >= k:
                res.append(nums[index_dq[0]])
                l += 1
            r += 1

        return res