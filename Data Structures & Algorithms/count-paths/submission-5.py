class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Memoization (top-down approach) - time complexity: O(n * m), space complexity: O(n * m)
        cache_grid = [[0] * n for _ in range(m)]

        def memo(row: int, col: int) -> int:
            if row >= m or col >= n:
                return 0
            if cache_grid[row][col] > 0:
                return cache_grid[row][col]
            if row == m - 1 and col == n - 1:
                return 1
            
            cache_grid[row][col] = memo(row + 1, col) + memo(row, col + 1)
            return cache_grid[row][col]

        return memo(0, 0)