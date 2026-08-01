class MinStack:
    # perfect solution
    def __init__(self):
        self.encoded_stack = []
        self.curr_min = float('inf')

    def push(self, val: int) -> None:
        if not self.encoded_stack:
            self.encoded_stack.append(0)
            self.curr_min = val
            return

        encoded_val = val - self.curr_min
        self.encoded_stack.append(encoded_val)
        if encoded_val < 0:
            self.curr_min = val

    def pop(self) -> None:
        encoded_top = self.encoded_stack.pop()
        if encoded_top < 0:
            self.curr_min -= encoded_top

    def top(self) -> int:
        encoded_top = self.encoded_stack[-1]
        if encoded_top < 0:
            return self.curr_min
        
        return self.curr_min + encoded_top

    def getMin(self) -> int:
        return self.curr_min
