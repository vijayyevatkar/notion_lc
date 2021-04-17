class Solution {
    public int rob(int[] nums) {

        int l = nums.length;

        // Handle base conditions
        if(l==0) return 0;
        if(l==1) return nums[0];

        int prevMax = nums[0]; // this denotes the maximum value till index 0
        int currMax = Math.max(nums[0],nums[1]); // this denotes the maximum value till index 1
        int tempMax = -1; // can initialize to anything, doesn't matter

        // from index 2 onwards, we will iteratively update our prevMax and currMax
        for(int i = 2; i<l; i++) {
            // at any given i, the maximum value that can be robbed till i
            tempMax = Math.max(prevMax+nums[i],currMax);
            
            // now for next iteration, i will be i+1, hence
            prevMax = currMax; // our prevMax, which belonged to max till i-2, will now be max till i-1
            currMax = tempMax; // and our currMax, which was max till i-1, will now be max till i
        }
        return currMax;
        
    }
}