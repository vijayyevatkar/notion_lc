class Solution {
    public int maxProfit(int[] prices) {
        
        int l = prices.length;

        // Can't buy and sell on different days if we have less than 2 entries
        if (l<2) return 0;
        int answer = 0;

        // start by assuming that the lowest price is that of day 1
        int currLow = prices[0];
        
        for(int i=1; i<l; i++) {

            // on any subsequent day, if you find a price greater than the currentLow price, 
            //     calculate the profit and update answer if that profit is greater
            if(prices[i]>currLow) {
                int temp = prices[i] - currLow;
                answer = Math.max(temp,answer);
            } else {
                // else, if you find a lower price, just update your currentLow as this is your new low!
                currLow = prices[i];
            }
        }
        return answer;
    }
}