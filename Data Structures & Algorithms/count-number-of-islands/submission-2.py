class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        res = 0

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(r, c):
            q = deque([(r, c)])
            grid[r][c] = "0"

            while q:
                curr_row, curr_col = q.popleft()
                for dr, dc in directions:
                    nei_row, nei_col = curr_row + dr, curr_col + dc
                    if (0 <= nei_row < m and
                        0 <= nei_col < n and
                        grid[nei_row][nei_col] == "1"):
                        q.append((nei_row, nei_col))
                        grid[nei_row][nei_col] = "0"

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    bfs(r, c)
                    res += 1

        return res
            