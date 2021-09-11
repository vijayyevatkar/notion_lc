class Solution {
    public boolean reachingPoints(int sx, int sy, int tx, int ty) {

        // Recursive Solution:
        // return reachUsingRecursion(int sx, int sy, int tx, int ty);

        // Time Optimized Solution:
        return reachUsingModulo(sx, sy, tx, ty);

    }

    public boolean reachUsingModulo(int sx, int sy, int tx, int ty) {
        // Loop until you reach the top of the tree -> the source, the root
        while(tx >= sx && ty >= sy) {
            if (tx > ty) {
                // if x coordinate has reached its source, just check if y coordinate can be reached using x
                if (sy == ty) return (tx-sx) % sy == 0;
                tx = tx % ty;
            } else {
                // if y coordinate has reached its source, just check if x coordinate can be reached using y
                if (sx == tx) return (ty-sy) % sx == 0;
                ty = ty % tx;
            }
        }
        return false;
    }

    public boolean reachUsingRecursion(int sx, int sy, int tx, int ty) {
        // Stop recursion base conditions
        if(sx==tx && sy==ty) return true;
        if(sx==0 && sy==0 && (tx!=sx || ty!=sy)) return false;
        if(sx>tx || sy>ty) return false;
        
        // Recurse on both children
        return reachUsingRecursion(sx+sy,sy,tx,ty) || reachUsingRecursion(sx,sx+sy,tx,ty);
    }
}