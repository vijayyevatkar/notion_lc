class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix),len(matrix[0])
        l = m*n
        return self.binarySearch(matrix,target,0,l-1,n)
        
    def binarySearch(self,matrix:List[List[int]],target:int,start:int,end:int,n:int) -> bool:
        
        if start > end or start < 0:
            return False
        mid = start + int((end-start)/2)
        # print(f"Start, end, n: {start},{end},{n}")
        i = int(mid/n)
        j = int(mid%n)
        # print(f"i, j: {i},{j}")
        if matrix[i][j] == target:
            return True
        if matrix[i][j] < target:
            return self.binarySearch(matrix,target,mid+1,end,n)
        return self.binarySearch(matrix,target,start,mid-1,n)
        