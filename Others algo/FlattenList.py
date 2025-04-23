class Solution:
    def flatten(self, *args):
        newList = []
        for arg in args:
            if isinstance(arg, list):
                for e in arg:
                    newList += self.flatten(e)
            else:
                newList.append(arg)
        return newList


if __name__ == "__main__":
    solution = Solution()
    print(solution.flatten(1, 4, [2, 3], 4, 5, [6, [7]]))