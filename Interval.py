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


class Solution2():
    def findInterval(self, intervals, points):
        numberOfPointsInInterval = [0] * (len(intervals) - 1)
        points.sort()
        for point in points:
            l = 0
            r = len(intervals) - 1
            if intervals[l] > point or intervals[r] < point:
                continue
            while l < r:
                m = (l + r) // 2
                if point > intervals[m]:
                    l = m + 1
                if point <= intervals[m]:
                    r = m

            if intervals[l] > point:
                numberOfPointsInInterval[l - 1] += 1
            else:
                numberOfPointsInInterval[l] += 1

        return numberOfPointsInInterval


if __name__ == '__main__':
    sol = Solution2()
    intervals = [1, 4, 7, 10, 20]
    points = [1, 2.5, 4.5, 6, 7.9, 12.3, 15, 21]
    print(sol.findInterval(intervals, points))
