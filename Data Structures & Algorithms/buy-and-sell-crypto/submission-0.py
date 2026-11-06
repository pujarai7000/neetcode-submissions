class Solution:
    def maxProfit(self, prices: List[int]) -> int:
     lowest=prices[0]
     max_profit=0
     for num in prices:
        if num<lowest :
            lowest=num
        profit=num - lowest 
        if max_profit < profit:
          max_profit=profit 
     return max_profit