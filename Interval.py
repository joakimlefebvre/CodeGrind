class Solution():
    def findInterval(self, intervals, points):
        numberOfPointsInInterval = [0] * (len(intervals) - 1)
        points.sort()
        j = 0
        for i in range(len(intervals) - 1):
            while j < len(points) and intervals[i] <= points[j] < intervals[i + 1]:
                numberOfPointsInInterval[i] += 1
                j += 1
        return numberOfPointsInInterval


if __name__ == '__main__':
    sol = Solution()
    intervals = [1, 4, 10, 15, 20]
    points = [1.4, 2.5, 12.3, 15]
    print(sol.findInterval(intervals, points))
