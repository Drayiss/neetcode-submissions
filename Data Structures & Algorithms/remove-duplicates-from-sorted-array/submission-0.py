class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(0, len(nums)):
            if (nums[i] != nums[k - 1]):
                temp = nums[i]
                nums[i] = nums[k]
                nums[k] = temp
                k += 1
        return k
