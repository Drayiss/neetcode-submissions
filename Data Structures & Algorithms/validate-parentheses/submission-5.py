class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        close_to_open_dict = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in close_to_open_dict:
                if my_stack and my_stack[-1] == close_to_open_dict[c]:
                    my_stack.pop()
                else:
                    return False
            else:
                my_stack.append(c)

        return True if not my_stack else False