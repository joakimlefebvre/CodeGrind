class Solution:
    def greatestLetter(self, s: str) -> str:
        check = set(s)

        for i in range(ord('Z'), ord('A') - 1, -1):
            letter = chr(i)
            if letter in check and letter.lower() in check:
                return letter
        return ""


if __name__ == "__main__":
    sol = Solution()
    s = "arRAzFif"
    print(sol.greatestLetter(s))
