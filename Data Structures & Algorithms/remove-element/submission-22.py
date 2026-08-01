class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(0, len(nums)):
            nums[k] = nums[i]
            if nums[k] != val:
                k += 1

        return k