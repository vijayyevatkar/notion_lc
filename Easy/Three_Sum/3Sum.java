class Solution {
    public List<List<Integer>> threeSum(int[] nums) {

        int l = nums.length;
        List<List<Integer>> answer = new ArrayList();
        if (l<3) return answer;

        // Sort the input
        Arrays.sort(nums);
        int target = 0;

        for (int i = 0; i<l-2; i++) {
            // at any point, if we encounter the same number as previous one, ignore it as we would've already found all the triplets for that target
            if(i>0 && nums[i]==nums[i-1]) continue;
            target = -nums[i];

            // Search in range from i+1 to end of the array for the pair that matches target
            int j = i+1;
            int k = l-1;

            // we can stop if j and k cross each other
            while(j<l && k>=0 && j<k) {
                if(nums[j]+nums[k]>target) k-=1;
                else if(nums[j]+nums[k]<target) j+=1;
                else {
                    List<Integer> tempList = new ArrayList();
                    tempList.add(-target);
                    tempList.add(nums[j]);
                    tempList.add(nums[k]);
                    answer.add(tempList);
                    j+=1;
                    k-=1;

                    // skip all the nums with same value as we need distinct triplets
                    while(j<l && nums[j]==nums[j-1]) j+=1;
                    while(k>=0 && nums[k]==nums[k+1]) k-=1;
                }
            }
        }
        return answer;
    }
}