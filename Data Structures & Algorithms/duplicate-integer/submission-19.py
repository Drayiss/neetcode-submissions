class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}

        for i, num in enumerate(nums):
            count[num] = 1 + count.get(num, 0)
        
        for key, value in count.items():
            if value > 1:
                return True

        return False