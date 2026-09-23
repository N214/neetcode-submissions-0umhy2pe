class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices) -1):
            if prices[i] < prices[i+1]:
                # buy
                print(f"price of {i} is {prices[i]}, price of {i+1} is {prices[i+1]},")
                profit = prices[i+1] - prices[i]
                print(f"profit of my transaction is {profit}")
                res += profit
            
        return res