'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=float('inf')
        max_profit=0

        for price in prices:
            if price<min_price:
                min_price=price
            elif price-min_price>max_profit:
                    max_profit=profit
        
        return max_profit

'''
Solution explanation:

Here min price starts at infinity and max price starts at 0. For each price, if it is less than min price, then min price is updated. Else, profit is measured. If profit is greater than current max profit, max 
profit is updated to current profit. The if condition for profit is used since the most minimum price does not ensure biggest profit. Eg: Assume [5,2,3,4,8,1,5,4]. Here, min price is 1, but it gives a max profit
of 4(ie, 5-1). 6(ie,8-2) is the highest profite obtainable. We return the maximum profit.
'''
