class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open parenthesis if open < n
        # only add closed parenthesis if closed < open
        # valid IIF open == closed == n

        stack = []
        res = []

        def back_track(open_num: int, closed_num: int):
            if open_num == closed_num == n:
                res.append("".join(stack))
                return
            
            if open_num < n:
                stack.append('(')
                back_track(open_num + 1, closed_num)
                stack.pop()

            if closed_num < open_num:
                stack.append(')')
                back_track(open_num, closed_num + 1)
                stack.pop()
        
        back_track(0, 0)
        return res