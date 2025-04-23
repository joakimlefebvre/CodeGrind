class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high+1):
            num = str(i)
            n = len(num)
            if n%2 == 0:
                left_side = sum(int(digit) for digit in num[:n//2])
                right_side = sum(int(digit) for digit in num[n // 2:])
                if left_side == right_side:
                    count += 1

        return count

s = Solution()
print(s.countSymmetricIntegers(1,100))