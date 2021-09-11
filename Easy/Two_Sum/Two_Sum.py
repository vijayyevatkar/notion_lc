class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Problem statement - You may assume that each input would have exactly one solution
        #Hence, Base condition check - not required
        return Solution.optimalSolution(self, nums,target);
        #return Solution.bruteForceSolution(self,nums,target);

    def bruteForceSolution(self, nums: List[int], target: int) -> List[int]:
        #Declarations
        l = len(nums)
        ans = [] 
        stop = False

        for i in range(0,l-1):
            for j in range(i+1,l):
                if nums[i]+nums[j]==target:
                    ans.append(i)
                    ans.append(j)
                    stop = True
                if stop:
                    break
            if stop:
                break
        return ans;

    def optimalSolution(self, nums: List[int], target: int) -> List[int]:
        #Declarations
        l = len(nums)
        ans = [] 
        stop = False

        # Step 1 -> Build Hashmap
        map = Solution.buildHashMap(self,nums)

        # Step 2 -> Sort
        # Internally uses tim sort => O(nlogn)
        nums.sort() 
        
        # Step 3 -> Two Pointer
        i=0
        j=l-1
        while not stop:
            if nums[i]+nums[j]==target:
                li = map[nums[i]]
                ans.append(li.pop(0))
                li = map[nums[j]]
                ans.append(li.pop(0))
                stop = True
            elif nums[i]+nums[j]<target:
                i+=1
            else:
                j-=1
        
        return ans; 

    def buildHashMap(self, nums: List[int]) -> dict():
        # Store array of indices, pop them when getting
        hm = {}
        for i in range(0,len(nums)):
            temp = []
            if nums[i] in hm:
                temp = hm[nums[i]]
            temp.append(i)
            hm[nums[i]] = temp
        return hm