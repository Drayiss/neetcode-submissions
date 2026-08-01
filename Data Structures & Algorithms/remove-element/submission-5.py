class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0

        # while l < len(nums) and nums[l] != val:
        #     l += 1
        #     r = l + 1
        #     if r >= len(nums):
        #         break
        #     while r < len(nums) and nums[r] == val:
        #         r += 1
        #     nums[l] = nums[r]
        #     nums[r] = val
        while l < len(nums) and nums[l] != val:
            l += 1

        for r in range(l + 1, len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                nums[r] = val
                l += 1

            
            
            
        return l
        
            
