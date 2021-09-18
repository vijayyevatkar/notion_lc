# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return self.maxDepthRec(root,1)
    
    def maxDepthRec(self, root: Optional[TreeNode], depth: int) -> int:
        
        if not root:
            return depth
        left = depth
        right = depth
        if root.left:
            left = self.maxDepthRec(root.left,depth+1)
        if root.right:
            right = self.maxDepthRec(root.right,depth+1)
        return max(left,right)
    