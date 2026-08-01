class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # my_set = set()
        
        # for num in nums:
        #     if num in my_set:
        #         return True
        #     my_set.add(num)
        # return False
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                return True
        return False