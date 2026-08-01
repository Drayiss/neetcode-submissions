class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 2D DP solution (bottom-up approach) - time complexity: O(m * n), space complexity: O(n)
        prev_row = [1] * n

        for _ in range(m - 2, -1, -1):
            curr_row = [1] * n

            for col in range(n - 2, -1, -1):
                curr_row[col] = prev_row[col] + curr_row[col + 1]

            prev_row = curr_row
        
        return prev_row[0]