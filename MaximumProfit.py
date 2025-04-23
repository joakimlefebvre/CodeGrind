class Solution():
    def getMaximumProfit(self, n, price, profit):
        maxProfit = 0
        for i in range(n):
            lMax, rMax = 0, 0
            for j in range(i):
                if price[j] < price[i]:
                    lMax = max(lMax, profit[j])
            for j in range(i + 1, n):
                if price[j] > price[i]:
                    rMax = max(rMax, profit[j])
            if lMax and rMax:
                maxProfit = max(maxProfit, lMax + rMax + profit[i])
        return maxProfit


class Solution2():
    def getMaximumProfit(self, price, profit):
        n = len(price)
        left_max = [-1] * n
        right_max = [-1] * n

        # Left max: max profit[i] for i < j and price[i] < price[j]
        min_price_indices = []
        for j in range(n):
            max_profit = -1
            for i in min_price_indices:
                if price[i] < price[j]:
                    max_profit = max(max_profit, profit[i])
            left_max[j] = max_profit
            min_price_indices.append(j)

        # Right max: max profit[k] for k > j and price[j] < price[k]
        max_price_indices = []
        for j in range(n-1, 0, -1):
            max_profit = -1
            for k in max_price_indices:
                if price[j] < price[k]:
                    max_profit = max(max_profit, profit[k])
            right_max[j] = max_profit
            max_price_indices.append(j)

        # Combine results
        max_total = -1
        for j in range(n):
            if left_max[j] != -1 and right_max[j] != -1:
                max_total = max(max_total, left_max[j] + profit[j] + right_max[j])

        return max_total


if __name__ == "__main__":
    sol = Solution2()
    n = 5
    price = [1, 5, 3, 4, 6]
    profit = [2, 3, 4, 5, 6]
    print(sol.getMaximumProfit(price, profit))
