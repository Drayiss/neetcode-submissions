class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = count = 0

        for num in nums:
            if num:
                count += 1
            else:
                count = 0
            res = max(res, count)

        return res