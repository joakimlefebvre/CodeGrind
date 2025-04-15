from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0
        for i in range(len(timeSeries)-1):
            if timeSeries[i+1] - timeSeries[i] < duration:
                total += timeSeries[i+1] - timeSeries[i]
            else:
                total += duration
        total += duration
        return total

if __name__ == '__main__':
    solution = Solution()
    timeSeries = [1,2]
    duration = 2
    print(solution.findPoisonedDuration(timeSeries, duration))