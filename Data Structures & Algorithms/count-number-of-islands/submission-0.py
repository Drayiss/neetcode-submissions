from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        total_rows = len(grid)
        total_cols = len(grid[0])

        seen = set()

        res = 0

        def bfs(cell):
            q = deque()
            seen.add(cell)
            q.append(cell)

            while q:
                row, col = q.popleft()
                
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nr, nc = dr + row, dc + col
                    if (not 0 <= nr < total_rows
                        or not 0 <= nc < total_cols
                        or grid[nr][nc] == '0'
                        or (nr, nc) in seen):
                        continue
                    
                    seen.add((nr, nc))
                    q.append((nr, nc))
                    

        for row in range(total_rows):
            for col in range(total_cols):
                curr_cell = grid[row][col]
                if curr_cell == '1' and (row, col) not in seen:
                    bfs((row, col))
                    res += 1

        return res
        
