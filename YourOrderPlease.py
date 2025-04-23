class Solution():
    def order(self, s):
        words = s.split()
        newS = [""] * len(words)
        for w in words:
            for char in w:
                if char.isdigit():
                    position = int(char)
                    newS[position-1] = w
        return ' '.join(newS)


if __name__ == "__main__":
    solution = Solution()
    s = "is2 Thi1s T4est 3a"
    print(solution.order(s))
