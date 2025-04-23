from typing import List


class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        '''
        Logic: Split into two arrays - odds and evens. Find beautiful array for each and merge them
        To merge, reverse the solution of 'odds' array and then append the solution of 'even' to that

        Illustrating with an example
        n = 9 -> [1 2 3 4 5 6 7 8 9]    -> Solution [5 1 9 3 7 6 2 4 8]    (From Level 0)

        Level 1 (Odd)  - (1 3 5 7 9)    -> Solution [7 3 9 1 5] (From Level 2)
        Level 1 (Even) - (2 4 6 8)      -> Solution [6 2 4 8]   (From Level 4)
        Level 2 (Odd)  - (3 7)          -> Solution [3 7]       (End Condition)
        Level 2 (Even) - (1 5 9)        -> Solution [9 1 5]     (From Level 3)
        Level 3 (Odd)  - (5)            -> Solution [5]         (End Condition)
        Level 3 (Even) - (1 9)          -> Solution [1 9]       (End Condition)
        Level 4 (Odd)  - (2 6)          -> Solution [2 6]       (End Condition)
        Level 4 (Even) - (4 8)          -> SOlution [4 8]       (End Condition)
        '''
        if n <= 2:
            return list(range(1, n + 1))
        elif n == 3:
            return [3, 1, 2]
        elif n == 4:
            return [3, 1, 2, 4]
        else:
            evens = self.beautifulArray(n // 2)
            odds = self.beautifulArray(n - n // 2)
            return [2 * x - 1 for x in reversed(odds)] + [2 * x for x in evens]


if __name__ == "__main__":
    sol = Solution()
    n = 10
    print(sol.beautifulArray(n))
