from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_dict = defaultdict(set)
        cols_dict = defaultdict(set)
        squares_dict = defaultdict(set)

        for row in range(9):
            for col in range(9):
                current_cell = board[row][col]
                if current_cell == ".":
                    continue

                if (current_cell in rows_dict[row] or
                   current_cell in cols_dict[col] or
                   current_cell in squares_dict[(row // 3, col // 3)]):
                    return False
                
                rows_dict[row].add(current_cell)
                cols_dict[col].add(current_cell)
                squares_dict[(row // 3, col // 3)].add(current_cell)
        
        return True