class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, combination = [], []
        n = len(nums)

        def backtrack(i, curr_sum):
            if curr_sum == target:
                res.append(combination.copy())
                return
            
            if curr_sum > target or i == n:
                return
            
            # Don't pick nums[i]
            backtrack(i + 1, curr_sum)

            # Pick nums[i]
            pick = nums[i]
            combination.append(pick)
            backtrack(i, curr_sum + pick)
            combination.pop()
        
        backtrack(0, 0)
        return res
