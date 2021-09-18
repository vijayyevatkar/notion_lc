class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        l = len(triangle)        
        for i in range(l-1,0,-1):
            for j in range(1,len(triangle[i])):
                # print(f"triangle[{i}][{j}] = {triangle[i][j]}")
                triangle[i-1][j-1] += min(triangle[i][j], triangle[i][j-1])
        return triangle[0][0]