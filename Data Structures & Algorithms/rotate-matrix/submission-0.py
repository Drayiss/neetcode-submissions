class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix) # Matrix is n x n

        # Transpose
        for row in range(n):
            for col in range(row + 1, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        # Horizontal Reflection across vertical axis
        for row in range(n):
            for l in range(n // 2):
                r = n - 1 - l
                matrix[row][l], matrix[row][r] = matrix[row][r], matrix[row][l]