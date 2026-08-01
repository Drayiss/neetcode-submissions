class MinStack:
    # [0, 3]
    # min = 5

    def __init__(self):
        self.stack = []
        self.min = float("inf")

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
            return
        self.stack.append(val - self.min)
        self.min = min(val, self.min)

    def pop(self) -> None:
        tmp = self.stack.pop()

        # self.min = self.min - tmp if tmp < 0 else self.min

        if tmp < 0:
            self.min = self.min - tmp

    def top(self) -> int:
        encodedTop = self.stack[-1]
        if encodedTop > 0:
            return encodedTop + self.min
        return self.min

    def getMin(self) -> int:
        return self.min
        
