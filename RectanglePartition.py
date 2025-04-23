class Solution():
    def rectanglePartition(self, x, y, mx, my):
        mx = mx + [0] + [x]
        my = my + [0] + [y]
        mx.sort()
        my.sort()
        xSize = []
        ySize = []
        my.reverse()
        mx.reverse()
        for i, num in enumerate(my):
            for j in my[i + 1:len(my)]:
                ySize.append(num - j)
        for i, num in enumerate(mx):
            for j in mx[i + 1:len(mx)]:
                xSize.append(num - j)
        xSize.sort()
        ySize.sort()
        nbSquares = 0
        if len(xSize) > len(ySize):
            for num in ySize:
                if num in xSize:
                    nbSquares += 1 * max(ySize.count(num), xSize.count(num))
        else:
            for num in xSize:
                if num in ySize:
                    nbSquares += 1 * max(ySize.count(num), xSize.count(num))

        return nbSquares


if __name__ == "__main__":
    solution = Solution()
    x = 10
    y = 5
    mx = [2, 5]
    my = [3]
    print(solution.rectanglePartition(x, y, mx, my))
