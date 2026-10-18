class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        return max(
            self.helper(nums[:-1]),
            self.helper(nums[1:])
        )

    def helper(self, arr):
        n = len(arr)

        if n == 1:
            return arr[0]
        
        if n == 2:
            return max(arr[0], arr[1])

        prev = arr[0]
        curr = max(arr[0], arr[1])

        for i in range(2, n):
            prev, curr = curr, max(
                curr,
                arr[i] + prev
            )

        return curr
                
            