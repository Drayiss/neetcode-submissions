from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for key, value in Counter(nums).items():
            if value > 1:
                return True
        
        return False