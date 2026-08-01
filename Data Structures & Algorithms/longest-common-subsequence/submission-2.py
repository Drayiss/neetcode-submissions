class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Time complexity: O(n * m)
        # Space complexity: O(m)
        # n refers to length of text1, m refers to length of text2
        bottom_row = [0] * (len(text2) + 1)

        for row in range(len(text1) - 1, -1, -1):
            top_row = [0] * (len(text2) + 1)

            for col in range(len(text2) - 1, -1, -1):
                if text1[row] == text2[col]:
                    top_row[col] = 1 + bottom_row[col + 1]
                else:
                    top_row[col] = max(bottom_row[col], top_row[col + 1])

            bottom_row = top_row

        return top_row[0]