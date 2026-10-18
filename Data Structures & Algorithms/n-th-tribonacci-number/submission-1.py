class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0 : 0, 1 : 1, 2 : 1}

        def helper(n):
            if n in memo:
                return memo[n]
            
            memo[n] = helper(n - 3) + helper(n - 2) + helper(n - 1)
            return memo[n]
        
        return helper(n)