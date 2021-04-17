class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l==1:
            return nums[0]
        if l==2:
            return max(nums[0],nums[1])

        sumArray = [nums[0],max(nums[0],nums[1])]
        i = 2
        while i<l:
            sumArray.append(max(sumArray[i-2]+nums[i],sumArray[i-1]))
            i+=1
        return sumArray[l-1]