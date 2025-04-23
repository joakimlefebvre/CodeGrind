class Solution:
    def longestValidParentheses(self, s: str) -> int:
        lCount = rCount = maxLen = 0

        i = 0

        while i < len(s):
            if s[i] == "(":
                lCount += 1
            else:
                rCount += 1

            if lCount == rCount:
                maxLen = max(maxLen, lCount, rCount)
            elif rCount > lCount:
                lCount = rCount = 0
            i += 1

        lCount = rCount = 0
        i = len(s) - 1

        while i >= 0:
            if s[i] == "(":
                lCount += 1
            else:
                rCount += 1

            if lCount == rCount:
                maxLen = max(maxLen, lCount, rCount)
            elif lCount > rCount:
                lCount = rCount = 0
            i -= 1
        return maxLen*2


if __name__ == "__main__":
    sol = Solution()
    s = "()(()"
    print(sol.longestValidParentheses(s))
