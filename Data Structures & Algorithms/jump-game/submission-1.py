from collections import defaultdict

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = {n - 1 : True}

        def can_reach_end(i):
            if i == n - 1:
                return True

            if i in dp:
                return dp[i]
            
            for jump in range(i + 1, i + nums[i] + 1):
                if can_reach_end(jump):
                    dp[jump] = True
                    return True
            
            dp[i] = False
            return False
        
        return can_reach_end(0)