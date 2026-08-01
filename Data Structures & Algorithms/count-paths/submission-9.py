class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 2D DP solution (bottom-up approach) - time complexity: O(m * n), space complexity: O(n)
        # Fully optimized
        curr_row = [1] * n

        for row in range(m - 2, -1, -1):
            for col in range(n - 2, -1, -1):
                curr_row[col] += curr_row[col + 1]
        
        return curr_row[0]