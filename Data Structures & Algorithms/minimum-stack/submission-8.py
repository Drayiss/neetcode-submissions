class MinStack:
    # perfect solution

    def __init__(self):
        self.encodedStack = []
        self.currMin = float('inf')

    def push(self, val: int) -> None:
        if not self.encodedStack:
            self.encodedStack.append(0)
            self.currMin = val
            return
        
        encodedVal = val - self.currMin
        self.encodedStack.append(val - self.currMin)
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
        return self.currMin + encodedTop

    def getMin(self) -> int:
        return self.currMin
