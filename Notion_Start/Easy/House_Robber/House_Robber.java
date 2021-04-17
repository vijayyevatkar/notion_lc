class Solution {
    public int rob(int[] nums) {

        int l = nums.length;
        if(l==0) return 0;
        if(l==1) return nums[0];
        int[] sumArray = new int[l];
        sumArray[0] = nums[0];
        sumArray[1] = Math.max(nums[0],nums[1]);
        if(l==2) return sumArray[1];

        for(int i = 2; i<l; i++) {
            sumArray[i] = Math.max(sumArray[i-2]+nums[i],sumArray[i-1]);
        }
        return sumArray[l-1];
        
    }
}