# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        if not root.right and not root.left:
            return [[root.val]]
        q = [root,"$"]
        answer = []
        currentLevel = []
        while len(q):
            elem = q.pop(0)
            if elem != "$":
                currentLevel.append(elem.val)
                if elem.left:
                    q.append(elem.left)
                if elem.right:
                    q.append(elem.right)
            else:
                if not len(currentLevel):
                    break
                answer.append(currentLevel)
                currentLevel = []
                q.append("$")
        return answer