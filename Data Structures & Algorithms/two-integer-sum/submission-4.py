class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffToIndex = {}

        for i, num in enumerate(nums):
            if num in diffToIndex:
                return [diffToIndex[num], i]
            diff = target - num
            diffToIndex[diff] = i
        
        return [0, 1]