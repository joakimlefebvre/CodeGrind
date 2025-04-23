from typing import List
from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # Check if it is out of bound
        def invalid(r,c):
            return r < 0 or c < 0 or r == n or c == n

        # In dfs we visit every possible position from [r,c]
        visit = set()
        def dfs(r, c):
            if invalid(r, c) or not grid[r][c] or (r, c) in visit:
                return
            visit.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        def bfs():
            # deque is a FIFO and LIFO queue
            res, q = 0, deque(visit)
            while q:
                for i in range(len(q)):
                    # Pop the leftmost [r,c] position we visited
                    r, c = q.popleft()
                    for dr, dc in directions:
                        curR, curC = r + dr, c + dc
                        if invalid(curR, curC) or (curR, curC) in visit:
                            continue
                        # if grid is a 1 !!
                        if grid[curR][curC]:
                            return res
                        q.append([curR, curC])
                        visit.add((curR, curC))
                res += 1

        for r in range(n):
            for c in range(n):
                if grid[r][c]:
                    dfs(r, c)
                    return bfs()

if __name__ == '__main__':
    solution = Solution()
    grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
    print(solution.shortestBridge(grid))