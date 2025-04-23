class Solution():
    def arrayChallenge(self, arr):
        arithmeticValue = arr[1]-arr[0]
        geometricValue = arr[1]/arr[0]
        arithmetic = True
        geometric = True
        for i in range(2, len(arr)):
            if arr[i]-arr[i-1] != arithmeticValue:
                arithmetic = False
            if arr[i]/arr[i-1] != geometricValue:
                geometric = False
            if not arithmetic and not geometric:
                break
        if arithmetic:
            return "Arithmetic"
        elif geometric:
            return "Geometric"
        else:
            return -1


if __name__ == "__main__":
    sol = Solution()
    arr = [2, 6, 10, 14, 18, 22, 26]
    print(sol.arrayChallenge(arr))
