# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.calculateSum(root,targetSum,0)
        
    def calculateSum(self, root: Optional[TreeNode], targetSum: int, currentSum: int) -> bool:
        
        tempSum = currentSum + root.val
        if tempSum == targetSum:
            if not root.left and not root.right:
                return True
        answer = False
        if root.left:
            answer = self.calculateSum(root.left,targetSum,tempSum)
        if not answer and root.right:
            answer = self.calculateSum(root.right,targetSum,tempSum)
        return answer