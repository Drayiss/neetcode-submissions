class MinStack:
    # [0, 0]
    # self.currMin = 5

    def __init__(self):
        self.encodedStack = []
        self.currMin = float('inf')

    def push(self, val: int) -> None:
        if not self.encodedStack:
            self.currMin = val
            self.encodedStack.append(0)
            return

        encodedVal = val - self.currMin
        self.encodedStack.append(encodedVal)
        if encodedVal < 0:
            self.currMin = val

    def pop(self) -> None:
        encodedTop = self.encodedStack.pop()
        if encodedTop < 0:
            self.currMin -= encodedTop

    def top(self) -> int:
        encodedTop = self.encodedStack[-1]
        if encodedTop < 0:
            return self.currMin
        return encodedTop + self.currMin

    def getMin(self) -> int:
        return self.currMin
