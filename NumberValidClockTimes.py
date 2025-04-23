class Solution:
    def countTime(self, time: str) -> int:
        hoursPossibilities = 1
        minutesPossibilities = 1
        if time[0] == "?" and time[1] == "?":
            hoursPossibilities = 24
        elif time[0] == "?" and int(time[1]) < 4:
            hoursPossibilities = 3
        elif time[1] == "?" and int(time[0]) < 2:
            hoursPossibilities = 10
        elif time[0] == "?":
            hoursPossibilities = 2
        elif time[1] == "?":
            hoursPossibilities = 4
        if time[3] == "?" and time[4] == "?":
            minutesPossibilities = 60
        elif time [3] == "?":
            minutesPossibilities = 6
        elif time[4] == "?":
            minutesPossibilities = 10
        return minutesPossibilities*hoursPossibilities


if __name__ == "__main__":
    sol = Solution()
    time = "0?:0?"
    print(sol.countTime(time))
