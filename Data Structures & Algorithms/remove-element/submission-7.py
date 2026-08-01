class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0

        while l < len(nums) and nums[l] != val:
            l += 1

        for r in range(l + 1, len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                nums[r] = val
                l += 1
            
        return l
        
            
