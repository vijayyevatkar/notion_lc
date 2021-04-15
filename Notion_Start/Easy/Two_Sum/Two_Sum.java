class Solution {
    public int[] twoSum(int[] nums, int target) {
        //Problem statement - You may assume that each input would have exactly one solution
        //Hence, Base condition check - not required
        return optimalSolution(nums,target);
        //return bruteForceSolution(nums,target);
    }

    public int[] bruteForceSolution(int[] nums, int target) {   
        //Declarations
        int l = nums.length;
        int[] ans = {0,0}; 
        boolean stop = false;

        for(int i=0; i<l-1; i++) {
            for (int j=i+1; j<l; j++) {
                if(nums[i]+nums[j]==target){
                    ans[0] = i;
                    ans[1] = j;
                    stop = true;
                }
                if(stop) break;
            }
            if(stop) break;
        }
        return ans;
    }

    public int[] optimalSolution(int[] nums, int target) {
        //Declarations
        int l = nums.length;
        int[] ans = {0,0}; 
        boolean stop = false;

        // Step 1 -> Build Hashmap
        HashMap<Integer,ArrayList<Integer> > map = buildHashMap(nums);

        // Step 2 -> Sort
        Arrays.sort(nums); // Internally uses merge sory => O(nlogn)
        // Step 3 -> Two Pointer
        int i=0, j=l-1;
        while(!stop) {
            if(nums[i]+nums[j]==target){
                ArrayList<Integer> li = map.get(nums[i]);
                ans[0] = li.remove(0);
                li = map.get(nums[j]);
                ans[1] = li.remove(0);
                stop = true;
            }
            else if(nums[i]+nums[j]<target){i+=1;}
            else {j-=1;}
        }
        return ans;    
    }

    public HashMap<Integer,ArrayList<Integer> > buildHashMap(int[] nums) {
        HashMap<Integer,ArrayList<Integer> > map = new HashMap<Integer,ArrayList<Integer> >();
        for(int i=0; i<nums.length; i++) {
            ArrayList<Integer> li = new ArrayList<Integer>();
            if(map.containsKey(nums[i])) {
                li = map.get(nums[i]);
            }
            li.add(i);
            map.put(nums[i],li);
        }
        return map;
    }

}