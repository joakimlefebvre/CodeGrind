class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()

if __name__ == '__main__':
    s = Solution()
    word = "FlaG"
    print(s.detectCapitalUse(word))