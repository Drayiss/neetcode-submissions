class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        right = 0

        while right < len(nums):
            right_val = nums[right]
            if right_val != val:
                nums[k] = right_val
                k += 1
            right += 1
        
        return k
            