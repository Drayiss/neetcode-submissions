class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_diff = {}

        for i in range(len(nums)):
            if nums[i] in target_diff:
                return [target_diff[nums[i]], i]
            diff = target - nums[i]
            target_diff[diff] = i

        return [-1, -1]