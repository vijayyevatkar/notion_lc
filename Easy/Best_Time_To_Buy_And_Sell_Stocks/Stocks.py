class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = len(prices)

        # Can't buy and sell on different days if we have less than 2 entries
        if l<2:
            return 0;
        
        answer = 0

        # start by assuming that the lowest price is that of day 1
        currLow = prices[0]

        # on any subsequent day, if you find a price greater than the currentLow price, 
        #     calculate the profit and update answer if that profit is greater
        for i in range(1,l):
            if prices[i]>currLow:
                answer = max(answer,prices[i]-currLow)
            else:
                # else, if you find a lower price, just update your currentLow as this is your new low!
                currLow = prices[i]
        
        return answer