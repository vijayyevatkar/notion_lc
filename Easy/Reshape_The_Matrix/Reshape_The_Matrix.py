class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        m = len(mat)
        n = len(mat[0])
        if m*n != r*c:
            return mat
        answer = []
        currList = []
        for i in range(m):
            for j in range(n):
                currList.append(mat[i][j])
                if len(currList) == c:
                    answer.append(currList)
                    currList = []
                    
        return answer