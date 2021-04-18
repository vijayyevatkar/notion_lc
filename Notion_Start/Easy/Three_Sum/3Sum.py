class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        l = len(nums)
        if l<3:
            return []
        
        # Sort the input
        nums.sort()
        answer = []

        for i in range(0,l-2):

            # at any point, if we encounter the same number as previous one, ignore it as we would've already found all the triplets for that target
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            # target will be negative of nums[i]
            target = -nums[i]

            # search in the range of i+1 to l-1
            j = i+1
            k = l-1

            # we can stop if j and k cross each other
            while j<l and k>0 and j<k:

                #basic 2sum logic
                if nums[j]+nums[k] < target:
                    j+=1
                elif nums[j]+nums[k] > target:
                    k-=1
                else:
                    tempList =[]
                    tempList.append(-target)
                    tempList.append(nums[j])
                    tempList.append(nums[k])
                    answer.append(tempList)
                    j+=1
                    k-=1

                    #skip all the nums with same value as we need distinct triplets
                    while j<l and nums[j]==nums[j-1]:
                        j+=1
                    while k>0 and nums[k]==nums[k+1]:
                        k-=1
        
        return answer