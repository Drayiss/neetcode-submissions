class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = []
        for i, num in enumerate(nums):
            sorted_nums.append([num, i])

        sorted_nums.sort()
        left, right = 0, len(nums) - 1

        while left < right:
            left_val = sorted_nums[left][0]
            left_index = sorted_nums[left][1]
            right_val = sorted_nums[right][0]
            right_index = sorted_nums[right][1]

            curr_sum = left_val + right_val
            if curr_sum == target:
                return [min(left_index, right_index), 
                        max(left_index, right_index)]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
        
        return []
