class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # Recursive Solution:
        # return Solution.reachUsingRecursion(self,int sx, int sy, int tx, int ty)

        # Time Optimized Solution:
        return Solution.reachUsingModulo(self,sx, sy, tx, ty)
        
    
    def reachUsingRecursion(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # Stop recursion base conditions
        if sx==tx and sy==ty:
            return True
        if sx>tx or sy>ty:
            return False
        
        # Recurse on both children
        return Solution.reachUsingRecursion(self,sx+sy,sy,tx,ty) or Solution.reachUsingRecursion(self,sx,sx+sy,tx,ty)

    def reachUsingModulo(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # Loop until you reach the top of the tree -> the source, the root
        while tx >= sx and ty >= sy:
            if tx > ty:
                # if x coordinate has reached its source, just check if y coordinate can be reached using x
                if sy == ty:
                    return (tx-sx) % sy == 0
                tx = tx % ty
            else:
                # if y coordinate has reached its source, just check if x coordinate can be reached using y
                if sx == tx:
                    return (ty-sy) % sx == 0
                ty = ty % tx
        return False