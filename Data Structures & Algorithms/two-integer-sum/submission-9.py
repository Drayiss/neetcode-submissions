class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # perfect solution
        diffToIndex = {}

        for i, num in enumerate(nums):
            if num in diffToIndex:
                return [diffToIndex[num], i]
            diff = target - num
            diffToIndex[diff] = i
        
        return [0, 1]