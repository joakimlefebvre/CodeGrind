from typing import List

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        capacity.sort(reverse=True)
        for i in range(len(capacity)):
            total -= capacity[i]
            if total <= 0:
                return i + 1
        return len(capacity)

if __name__ == '__main__':
    s = Solution()
    apple = [5,5,5]
    capacity = [2,4,2,7]
    print(s.minimumBoxes(apple, capacity))