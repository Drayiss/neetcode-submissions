
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        total_nums = len(nums)

        left = 0
        right = 0

        while right < total_nums:
            nums[left] = nums[right]
            while right < total_nums and nums[left] == nums[right]:
                right += 1
            left += 1

        return left