from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []

        for token in tokens:

            if token in operators:
                a1 = stack.pop()
                a2 = stack.pop()

                if token == "+":
                    stack.append(a1 + a2)
                elif token == "-":
                    stack.append(a2 - a1)
                elif token == "/":
                    stack.append(int(a2 / a1))
                elif token == "*":
                    stack.append(int(a1 * a2))
            else:
                stack.append(int(token))

        return stack.pop()


if __name__ == "__main__":
    solution = Solution()
    tokens = ["4", "-2", "/", "2", "-3", "-", "-"]
    print(solution.evalRPN(tokens))
