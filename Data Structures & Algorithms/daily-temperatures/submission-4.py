class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = temperatures
        n = len(temps)
        res = [0] * n
        index_stack = []
        # The stack will be ordered so that the lowest is at the top

        for i, temp in enumerate(temps):
            while index_stack and temps[index_stack[-1]] < temp:
                top_index = index_stack.pop()
                res[top_index] = i - top_index
            index_stack.append(i)
        
        return res