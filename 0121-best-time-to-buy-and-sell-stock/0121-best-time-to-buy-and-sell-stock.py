class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        Profit = 0
        for price in prices:
            if price < minPrice:
                minPrice = price
            elif price - minPrice > Profit:
                Profit = price - minPrice
        return Profit