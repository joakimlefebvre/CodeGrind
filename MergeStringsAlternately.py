class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        for a, b in zip(word1, word2):
            merged += a + b
        merged += (word1[len(word2):])
        merged += (word2[len(word1):])
        return merged


if __name__ == '__main__':
    s = Solution()
    word1 = "abcd"
    word2 = "pq"
    print(s.mergeAlternately(word1, word2))
