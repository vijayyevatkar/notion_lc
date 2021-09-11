class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not self.validateRow(board):
            return False
        if not self.validateColumn(board):
            return False
        m,n = len(board), len(board[0])
        for i in range(0,m,3):
            for j in range(0,n,3):
                if not self.validateBox(board,i,j):
                    return False
        return True
        
    def validateRow(self, board: List[List[str]]) -> bool:      
        for entries in board:
            entry = [int(i) for i in entries if i != "."]
            if len(entry) != len(set(entry)):
                return False
        return True
    
    def validateColumn(self, board: List[List[str]]) -> bool:    
        m,n = len(board), len(board[0])
        for j in range(n):
            entry = [int(board[i][j]) for i in range(m) if board[i][j] != "."]
            if len(entry) != len(set(entry)):
                return False
        return True
    
    def validateBox(self, board: List[List[str]], starti: int, startj: int) -> bool:
        
        entry = []
        for i in range(starti,starti+3):
            entry += [int(board[i][j]) for j in range(startj,startj+3) if board[i][j] != "."]
        if len(entry) != len(set(entry)):
            return False
        return True