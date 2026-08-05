class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        from collections import defaultdict

        if len(prices)==1:
            return 0

        stocks=defaultdict(int)

        for i in range(len(prices)-1):

            j=i+1
            while j<len(prices):
                profit=prices[j]-prices[i]
                if profit > stocks[i]:
                    stocks[i]=profit
                j+=1


        sell=max(stocks.values())
     
        if sell<0:
            return 0
        return sell        

        