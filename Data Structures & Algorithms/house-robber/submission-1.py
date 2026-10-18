class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]

        if n == 2:
            return max(nums[0], nums[1])

        memo = { 0 : nums[0], 1 : max(nums[0], nums[1]) }
        
        def opt(i):
            if i in memo:
                return memo[i]

            memo[i] = max(opt(i - 1), nums[i] + opt(i - 2))
            return memo[i]
        
        return opt(n - 1)
        