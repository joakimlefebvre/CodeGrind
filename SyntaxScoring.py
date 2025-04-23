class Solution():
    def syntaxScoring(self, s):
        points = {')': 3, ']': 57, '}': 1197, '>': 25137}
        openCharacter = ['(', '[', '{', '<']
        wrongCharacter = []
        for l in s:
            openC = []
            for c in l:
                if c in openCharacter:
                    openC.append(c)
                elif c == ')' and openC[-1] == '(':
                    openC.pop()
                elif c == ']' and openC[-1] == '[':
                    openC.pop()
                elif c == '}' and openC[-1] == '{':
                    openC.pop()
                elif c == '>' and openC[-1] == '<':
                    openC.pop()
                else:
                    wrongCharacter.append(c)
                    break
        score = 0
        for c in wrongCharacter:
            score += points[c]
        return score


if __name__ == "__main__":
    s = ["[({(<(())[]>[[{[]{<()<>>",
         "[(()[<>])]({[<{<<[]>>(",
         "{([(<{}[<>[]}>{[]{[(<()>",
         "(((({<>}<{<{<>}{[]{[]{}",
         "[[<[([]))<([[{}[[()]]]",
         "[{[{({}]{}}([{[{{{}}([]",
         "{<[[]]>}<{[{[{[]{()[[[]",
         "[<(<(<(<{}))><([]([]()",
         "<{([([[(<>()){}]>(<<{{",
         "<{([{{}}[<[[[<>{}]]]>[]]"]
    solution = Solution()
    print(solution.syntaxScoring(s))
