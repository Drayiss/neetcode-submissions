class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {0 : 0, 1 : 0}
        
        def calculate_cost(i):
            if i in memo:
                return memo[i]

            option_1 = calculate_cost(i - 1) + cost[i - 1]
            option_2 = calculate_cost(i - 2) + cost[i - 2]

            memo[i] = min(option_1, option_2)
            return memo[i]

        return calculate_cost(n)
        