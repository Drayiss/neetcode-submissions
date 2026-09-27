class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        res = 0

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(cell):
            r, c = cell
            q = deque([cell])
            grid[r][c] = "0"

            while q:
                curr_row, curr_col = q.popleft()
                for dr, dc in directions:
                    nr, nc = curr_row + dr, curr_col + dc
                    if (0 <= nr < m and
                        0 <= nc < n and
                        grid[nr][nc] == "1"):
                        n_cell = (nr, nc)
                        q.append(n_cell)
                        grid[nr][nc] = "0"

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    cell = (r, c)
                    bfs(cell)
                    res += 1

        return res
            