class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        dicoS = {}
        for char in s:
            if char in dicoS:
                dicoS[char] += 1
            else:
                dicoS[char] = 1
        middle = ""
        if n % 2 == 1:
            for key in dicoS.keys():
                if dicoS[key] % 2 == 1:
                    middle = key
        ans = []
        for key in sorted(dicoS.keys()):
            ans.append(key * (dicoS[key] // 2))
        return "".join(ans) + middle + "".join(ans[::-1])


if __name__ == "__main__":
    sol = Solution()
    s = "nhdhn"
    print(sol.smallestPalindrome(s))
