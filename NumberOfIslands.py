from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        numberOfIslands = 0

        def invalid(r,c):
            return r < 0 or c < 0 or r == m or c == n

        def dfs(r,c):
            if invalid(r,c) or int(grid[r][c]) != 1 or (r,c) in visited:
                return
            visited.add((r,c))

            for rD, cD in directions:
                dfs(r + rD, c + cD)
            return

        for r in range(m):
            for c in range(n):
                if int(grid[r][c]) and (r,c) not in visited:
                    dfs(r,c)
                    numberOfIslands += 1

        return numberOfIslands

if __name__ == '__main__':
    s = Solution()
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(s.numIslands(grid))