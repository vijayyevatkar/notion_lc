class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        answer = [s]
        l = len(s)
        prevList = []
        currList = []
        for ch in s:
            one = ch.lower()
            two = ch.upper()
            currList.append(one)
            if one != two:
                currList.append(two)
            if len(prevList):
                prevList = self.makePermutations(prevList,currList)
            else:
                prevList = currList[:]
            # print(prevList)
            currList = []
        return prevList
    
    def makePermutations(self, prevList: List[int], currList: List[int]) -> List[int]:
        
        answer = []
        for curr in currList:
            for prev in prevList:
                answer.append(prev+curr)
        return answer
                
        
    
    