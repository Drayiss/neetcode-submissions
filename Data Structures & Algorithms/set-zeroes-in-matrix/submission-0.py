class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        total_rows, total_cols = len(matrix), len(matrix[0])
        zero_row_zero = False
        
        # Set zero infoes
        for row in range(total_rows):
            for col in range(total_cols):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    if row == 0:
                        zero_row_zero = True
                    else:
                        matrix[row][0] = 0

        # Zero out rows and columns
        for row in range(1, total_rows):
            for col in range(1, total_cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
                
        # Zero out first col
        if matrix[0][0] == 0:
            for row in range(total_rows):
                matrix[row][0] = 0

        # Zero out first row
        if zero_row_zero:
            for col in range(total_cols):
                matrix[0][col] = 0
        