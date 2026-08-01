class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2) > len(text1):
            text1, text2 = text2, text1

        prev_row = [0] * (len(text2) + 1)

        for row in range(len(text1) - 1, -1, -1):
            curr_row = [0] * (len(text2) + 1)
            for col in range(len(text2) - 1, -1, -1):
                if text1[row] == text2[col]:
                    curr_row[col] = 1 + prev_row[col + 1]
                else:
                    curr_row[col] = max(prev_row[col], curr_row[col + 1])
            prev_row = curr_row
        
        return prev_row[0]

