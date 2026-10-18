from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        
        if n == 2:
            return max(nums[0], nums[1])

        @cache
        def opt(l, i):
            if i == l:
                return nums[l]
                
            if i == l + 1:
                return max(nums[l], nums[l + 1])

            return max(
                opt(l, i - 1),
                nums[i] + opt(l, i - 2)
            )

        return max(
            opt(0, n - 2),
            opt(1, n - 1)
        )

