class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        trackedValues = set()
        for num in nums:
            if num in trackedValues:
                return True
            trackedValues.add(num)
            
        return False