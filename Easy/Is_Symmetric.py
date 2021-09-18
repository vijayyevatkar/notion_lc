# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSym(root,root)
            
            
    def isSym(self, rootLeft: Optional[TreeNode], rootRight: Optional[TreeNode]) -> bool:
        
        if not rootLeft and not rootRight:
            return True
        
        if not rootLeft or not rootRight:
            return False
        
        return rootLeft.val == rootRight.val and self.isSym(rootLeft.left,rootRight.right) and self.isSym(rootLeft.right,rootRight.left)