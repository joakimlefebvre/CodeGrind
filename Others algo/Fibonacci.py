class Solution:
    def __init__(self):
        self.fSuite = [1, 2]

    def fibonacciSuite(self, n):
        if n == 1:
            return [1]
        elif n == 2:
            return [1, 2]
        elif n == 0:
            return None
        for i in range(2, n):
            self.fSuite.append(self.fSuite[i-2]+self.fSuite[i-1])
        return self.fSuite


if __name__ == "__main__":
    solution = Solution()
    print(solution.fibonacciSuite(100))
