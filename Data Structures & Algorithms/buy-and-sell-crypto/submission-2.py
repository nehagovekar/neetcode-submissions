class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #mistake 1: The sell day must come after the buy day. Calculating prices[i] - prices[j] where j > i means you're selling in the past, which is invalid.
        buy= 0
        sell= buy+1
        max_profit=0

        while(sell<len(prices)):
            if(prices[buy]>prices[sell]):
                buy = sell
            profit= prices[sell]- prices[buy]
            max_profit= max(max_profit,profit)
            #moving to the next day
            sell+=1
            
        return max_profit
            


        