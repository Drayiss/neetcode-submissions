class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # (index, height)

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                top_index, top_height = stack.pop()
                max_area = max(max_area, top_height * (i - top_index))
                start = top_index
            stack.append((start, height))

        while stack:
            top_index, top_height = stack.pop()
            max_area = max(max_area, top_height * (len(heights) - top_index))

        return max_area