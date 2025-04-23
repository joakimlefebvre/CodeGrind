import re


class Solution():
    def htmlVerification(self, html):
        htmlList = []
        i = 0
        while i < len(html):
            if html[i] == "<":
                j = html.find(">", i) + 1
                htmlList.append(html[i:j])
                i = j
            else:
                # Text content
                j = html.find("<", i)
                if j == -1:
                    htmlList.append(html[i:])
                    break
                else:
                    htmlList.append(html[i:j])
                    i = j
        print(htmlList)


if __name__ == "__main__":
    solution = Solution()
    html = "<h1><p>hello</p></h1>"
    solution.htmlVerification(html)
