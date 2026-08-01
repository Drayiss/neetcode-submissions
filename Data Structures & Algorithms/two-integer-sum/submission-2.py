class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for i, num in enumerate(nums):
            my_dict[target - num] = i
        
        for i, num in enumerate(nums):
            if num in my_dict:
                if my_dict[num] != i:
                    return [min(my_dict[num], i), max(my_dict[num], i)]
        return []
        