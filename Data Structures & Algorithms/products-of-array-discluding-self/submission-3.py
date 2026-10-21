class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = 1
        postfix = 1

        res = [1] * n

        for i in range(1, n):
            prefix *= nums[i - 1]
            res[i] *= prefix

        for i in range(n - 2, -1, -1):
            postfix *= nums[i + 1]
            res[i] *= postfix

        return res