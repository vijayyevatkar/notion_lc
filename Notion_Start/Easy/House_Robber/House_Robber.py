class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)

        # Handle base conditions
        if l==0:
            return 0
        if l==1:
            return nums[0]

        prevMax = nums[0] # this denotes the maximum value till index 0
        currMax = max(nums[0],nums[1]) # this denotes the maximum value till index 1

        # from index 2 onwards, we will iteratively update our prevMax and currMax
        i = 2
        while i<l:
            # at any given i, the maximum value that can be robbed till i
            tempMax = max(prevMax + nums[i], currMax)
            
            # now for next iteration, i will be i+1, hence
            prevMax = currMax # our prevMax, which belonged to max till i-2, will now be max till i-1
            currMax = tempMax # and our currMax, which was max till i-1, will now be max till i
            i+=1

        return currMax