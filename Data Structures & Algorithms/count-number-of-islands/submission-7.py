class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        res = 0

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        seen = set()

        def in_bounds(cell):
            r, c = cell
            return 0 <= r < m and 0 <= c < n

        def is_land(cell):
            r, c = cell
            return grid[r][c] == "1"

        def bfs(cell):
            q = deque([cell])
            seen.add(cell)

            while q:
                curr_row, curr_col = q.popleft()
                for dr, dc in directions:
                    nr, nc = curr_row + dr, curr_col + dc
                    n_cell = (nr, nc)
                    if (in_bounds(n_cell) and
                        is_land(n_cell) and
                        n_cell not in seen):
                        q.append(n_cell)
                        seen.add(n_cell)

        for r in range(m):
            for c in range(n):
                cell = (r, c)
                if is_land(cell) and cell not in seen:
                    bfs(cell)
                    res += 1

        return res
            