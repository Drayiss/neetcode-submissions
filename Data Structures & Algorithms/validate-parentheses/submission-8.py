class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            ']': '[',
            ')': '(',
            '}': '{'
        }

        stack = []
        for c in s:
            if c in closeToOpen:
                if len(stack) == 0:
                    return False
                if stack.pop() != closeToOpen[c]:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0