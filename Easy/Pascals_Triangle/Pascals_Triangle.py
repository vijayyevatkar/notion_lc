class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        answer = [[1]]
        for i in range(1,numRows):
            currList = [1]
            l = len(answer[i-1])
            if l > 1:
                for j in range(l-1):
                    currList.append(answer[i-1][j]+answer[i-1][j+1])
            currList.append(1)
            answer.append(currList)
        return answer