class Solution:
    def reformatNumber(self, number: str) -> str:
        listOfNumber = [char for char in number if char.isdigit()]
        newNumber = ""
        while len(listOfNumber) > 4:
            newNumber +=f"{listOfNumber[0]}{listOfNumber[1]}{listOfNumber[2]}-"
            for _ in range(3):
                listOfNumber.remove(listOfNumber[0])
        if len(listOfNumber) == 4:
            newNumber += f"{listOfNumber[0]}{listOfNumber[1]}-{listOfNumber[2]}{listOfNumber[3]}"
        elif len(listOfNumber) == 3:
            newNumber += f"{listOfNumber[0]}{listOfNumber[1]}{listOfNumber[2]}"
        elif len(listOfNumber) == 2:
            newNumber += f"{listOfNumber[0]}{listOfNumber[1]}"
        return newNumber

if __name__ == '__main__':
    solution = Solution()
    number = "123 4-5678"
    result = solution.reformatNumber(number)
    print(result)