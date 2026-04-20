"""
Problem: Best Time to Buy and Sell Stock
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Difficulty: Easy

Approach:
- Use two pointers (l = buy day, r = sell day)
- Move pointers to track minimum buying price
- Calculate profit and update maximum

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1

        return maxP
