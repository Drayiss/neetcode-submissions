class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # every element will be a pair (temperature, index)

        for index, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                top_temp, top_index = stack.pop()
                day_diff = index - top_index
                res[top_index] = day_diff

            stack.append((temp, index))

        return res