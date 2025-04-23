from collections import defaultdict
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {}

        def dfs(i, m, n):
            if i == len(strs):
                return 0
            if (i, m, n) in dp:
                return dp[(i, m, n)]
            mCount = strs[i].count("0")
            nCount = strs[i].count("1")
            dp[(i, m, n)] = dfs(i + 1, m, n)
            if mCount <= m and nCount <= n:
                dp[(i, m, n)] = max(
                    dp[(i, m, n)],
                    1 + dfs(i + 1, m - mCount, n - nCount))
            return dp[(i, m, n)]

        return dfs(0, m, n)


class Solution2:
    def findMaxForm(self, strs: List[str], M: int, N: int) -> int:
        dp = defaultdict(int)
        for s in strs:
            mCount, nCount = s.count("0"), s.count("1")
            for m in range(M, mCount - 1, -1):
                for n in range(N, nCount - 1, -1):
                    dp[(m, n)] = max(
                        1 + dp[(m - mCount, n - nCount)],
                        dp[(m, n)])
        return dp[(M, N)]


class Solution3:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Create a 2D DP array
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for s in strs:
            # Count zeros and ones in the current string
            zeros = s.count('0')
            ones = s.count('1')

            # Update DP table (iterate backwards to avoid counting the same item multiple times)
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)

        return dp[m][n]


if __name__ == '__main__':
    solution = Solution3()
    strs = ["10", "0001", "111001", "1", "0"]
    m = 4
    n = 3
    print(solution.findMaxForm(strs, m, n))
    # expected 3
