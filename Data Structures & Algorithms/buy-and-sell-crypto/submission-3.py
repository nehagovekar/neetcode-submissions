class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #in this code, it is a 2 pointer where we want to spend less price in buying and more in selling
        #Now, buying should always come before selling

        buy=0
        sell= buy+1
        #since we are moving pointers in the same direction different speeds so loop once
        max_profit= 0
        while(sell<len(prices)):
            if(prices[buy]>prices[sell]):
                buy=sell
            profit= prices[sell]- prices[buy]
            max_profit=max(max_profit, profit)

            #then move to the next sell
            sell+=1

        return max_profit
        