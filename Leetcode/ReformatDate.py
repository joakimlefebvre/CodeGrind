class Solution:
    def reformatDate(self, date: str) -> str:
        dicMonth = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06","Jul":"07","Aug":"08","Sep":"09","Oct":"10","Nov":"11","Dec":"12"}
        day, month, year = date.split()
        day = day[:-2]
        day = day.zfill(2)
        month = dicMonth[month]
        return f"{year}-{month}-{day}"
if __name__ == "__main__":
    sol = Solution()
    date = "6th Jun 1933"
    print(sol.reformatDate(date))