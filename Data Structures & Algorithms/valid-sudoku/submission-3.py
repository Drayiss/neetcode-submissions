from collections import defaultdict

class Solution:
    # perfect solution
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_to_seen = defaultdict(set)
        col_to_seen = defaultdict(set)
        square_to_seen = defaultdict(set)

        n = len(board)
        for row in range(n):
            for col in range(n):
                curr = board[row][col]

                if curr == ".":
                    continue

                square = (row // 3, col // 3)
                if (curr in row_to_seen[row] or
                    curr in col_to_seen[col] or
                    curr in square_to_seen[square]):
                    return False
                
                row_to_seen[row].add(curr)
                col_to_seen[col].add(curr)
                square_to_seen[square].add(curr)

        return True