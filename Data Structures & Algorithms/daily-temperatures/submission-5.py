class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = temperatures
        n = len(temps)
        res = [0] * n
        index_stack = []

        for i in range(n):
            curr = temps[i]
            while index_stack and temps[index_stack[-1]] < curr:
                top_index = index_stack.pop()
                res[top_index] = i - top_index
            index_stack.append(i)
        
        return res