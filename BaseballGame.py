from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        points = []
        for operation in operations:
            if operation == 'C':
                points.remove(points[-1])
            elif operation == 'D':
                points.append(points[-1] * 2)
            elif operation == '+':
                points.append(points[-1] + points[-2])
            else:
                points.append(int(operation))
        return sum(points)



if __name__ == '__main__':
    solution = Solution()
    ops = ["1","C"]
    print(solution.calPoints(ops))