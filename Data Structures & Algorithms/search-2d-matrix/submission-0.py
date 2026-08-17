class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bottom = 0, ROWS - 1
        curr_row = None

        while top <= bottom:
            curr_row = top - (top - bottom) // 2
            if target > matrix[curr_row][-1]:
                top = curr_row + 1
            elif target < matrix[curr_row][0]:
                bottom = curr_row - 1
            else:
                break
        
        if top > bottom:
            return False

        l, r = 0, COLS - 1
        while l <= r:
            mid = l - (l - r) // 2
            mid_val = matrix[curr_row][mid]
            if target > mid_val:
                l = mid + 1
            elif target < mid_val:
                r = mid - 1
            else:
                return True
        return False
