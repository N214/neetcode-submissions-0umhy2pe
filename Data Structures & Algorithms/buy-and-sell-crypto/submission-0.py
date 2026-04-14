class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointers L is buy and right is sell 
        l, r = 0, 1
        # you want to buy a min price 
        # you want to sell at max price
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP