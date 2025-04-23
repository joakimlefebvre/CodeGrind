from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]
        for i in range(numRows - 1):
            temp = [0] + rows[-1] + [0]
            row = []
            for j in range(len(rows[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            rows.append(row)
        return rows


if __name__ == '__main__':
    numRows = 5
    solution = Solution()
    print(solution.generate(numRows))
