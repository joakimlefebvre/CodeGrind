class Solution():
    def ipBetween(self, ip1, ip2):
        ip1, ip2 = ip1.split('.'), ip2.split('.')
        difference = 0
        for i in range(len(ip1)-1, 0, -1):
            difference += (int(ip1[i])-int(ip2[i]))*(256**(len(ip1)-1-i))
        return abs(difference)


if __name__ == "__main__":
    solution = Solution()
    ip1 = "10.11.12.13"
    ip2 = "10.11.13.0"
    print(solution.ipBetween(ip1, ip2))
