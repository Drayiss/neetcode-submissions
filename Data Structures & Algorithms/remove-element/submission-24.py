class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        right = len(nums) - 1

        while k <= right:
            if nums[k] == val:
                nums[k] = nums[right]
                right -= 1
            else:
                k += 1
        
        return k
            