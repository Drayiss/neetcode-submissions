class BrowserHistory:
    # perfect solution
    def __init__(self, homepage: str):
        self.curr_i = 0
        self.size = 1
        self.history = [homepage]

    def visit(self, url: str) -> None:
        self.curr_i += 1
        if self.curr_i == len(self.history):
            self.history.append(url)
        else:
            self.history[self.curr_i] = url
        self.size = self.curr_i + 1

    def back(self, steps: int) -> str:
        self.curr_i = max(self.curr_i - steps, 0)
        return self.history[self.curr_i]

    def forward(self, steps: int) -> str:
        self.curr_i = min(self.curr_i + steps, self.size - 1)
        return self.history[self.curr_i]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)