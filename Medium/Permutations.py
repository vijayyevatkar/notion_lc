class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        l = len(nums)
        if l == 1:
            return [[nums[0]]]
        return self.createPermutations(nums, 0, l)

    def createPermutations(self, nums: List[int], start: int, l: int) -> List[int]:

        if start == l:
            return []
        
        perms = self.createPermutations(nums, start+1, l)
        answer = []
        if len(perms):
            for perm in perms:
                k = len(perm)
                for pos in range(0,k+1):
                    currList = perm[:]
                    currList.insert(pos,nums[start])
                    answer.append(currList)
        else:
            answer.append([nums[start]])
        
        return answer


