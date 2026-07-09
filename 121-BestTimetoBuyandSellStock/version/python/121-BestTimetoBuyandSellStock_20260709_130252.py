# Last updated: 7/9/2026, 1:02:52 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        
4        mini = prices[0]
5        profit = 0
6
7        for i in range(1, len(prices)):
8            cost = prices[i] - mini
9            profit = max(profit, cost)
10            mini = min(mini, prices[i])
11        
12        return profit