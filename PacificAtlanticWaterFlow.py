from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        def f(s):
            v = set(s)
            q = list(s)
            while q:
                r, c = q.pop(0)
                for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    R, C = r + i, c + j
                    if 0 <= R < m and 0 <= C < n and (R, C) not in v and heights[R][C] >= heights[r][c]:
                        v.add((R, C))
                        q.append((R, C))
            return v

        p = [(x, 0) for x in range(m)] + [(0, x) for x in range(n)]
        a = [(x, n - 1) for x in range(m)] + [(m - 1, x) for x in range(n)]

        x = f(p)
        y = f(a)
        z = sorted(x.intersection(y))

        return [[r, c] for r, c in z]


if __name__ == "__main__":
    solution = Solution()
    heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    print(solution.pacificAtlantic(heights))
