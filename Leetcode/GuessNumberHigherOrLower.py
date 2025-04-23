def guess(num: int, pick) -> int:
    if num < pick:
        return 1
    elif num > pick:
        return -1
    else:
        return 0


class Solution:
    def guessNumber(self, n: int, pick) -> int:
        number = (1 + n) // 2
        a = 1
        b = n
        prev = float('inf')
        while prev != number:
            prev = number
            if guess(number, pick) == -1:
                b = number
                number = (a + b - 1) // 2
            elif guess(number, pick) == 1:
                a = number
                number = (a + b + 1) // 2
            else:
                pass
        return number


if __name__ == "__main__":
    solution = Solution()
    n = 2
    pick = 2
    print(solution.guessNumber(n, pick))
