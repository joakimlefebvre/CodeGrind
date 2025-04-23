from typing import List


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        nums = set(range(1, len(matrix)+1))
        for i in range(0, len(matrix)):
            row = matrix[i]
            col = [matrix[j][i] for j in range(0, len(matrix))]
            if nums.difference(set(row)) != set():
                return False
            elif nums.difference(set(col)) != set():
                return False
        return True


if __name__ == "__main__":
    matrix = [[1, 1], [1, 1]]
    solution = Solution()
    print(solution.checkValid(matrix))
