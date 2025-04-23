class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.minstack[-1]:
            self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


if __name__ == "__main__":
    obj = MinStack()
    actions = ["push", "push", "push", "getMin", "pop", "top", "getMin"]
    vals = [[-2], [0], [-3], [], [], [], []]
    for a, val in zip(actions, vals):
        if a == "push":
            print(obj.push(val[0]))
        elif a == "getMin":
            print(obj.getMin())
        elif a == "pop":
            print(obj.pop())
        elif a == "top":
            print(obj.top())