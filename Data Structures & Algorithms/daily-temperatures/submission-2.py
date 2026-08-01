class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # each element is a pair (temperature, index)

        for index, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                top_temp, top_index = stack.pop()
                res[top_index] = index - top_index

            stack.append((temp, index))
        
        return res
