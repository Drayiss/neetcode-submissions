class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * 2 * n
        for i in range(n):
            currValue = nums[i]
            ans[i] = currValue
            ans[i + n] = currValue
        return ans