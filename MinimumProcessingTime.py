from typing import List


class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()
        maxTime = 0
        for j, p in enumerate(processorTime):
            for i in range(4):
                time = p + tasks[i+4*j]
                if time > maxTime:
                    maxTime = time
        return maxTime


if __name__ == "__main__":
    processorTime = [8, 10]
    tasks = [2, 2, 3, 1, 8, 7, 4, 5]
    solution = Solution()
    print(solution.minProcessingTime(processorTime, tasks))
