# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        l = self.findLength(head)
        mid = int(l/2)
        currNode = 0
        traversalNode = head
        # print(traversalNode,l,mid,currNode)
        while traversalNode:
            if currNode == mid:
                break
            traversalNode = traversalNode.next
            currNode+=1
        return traversalNode
    
    def findLength(self, head: Optional[ListNode]) -> int:
        traversalNode = head
        answer = 0
        while traversalNode:
            traversalNode = traversalNode.next
            answer += 1
        return answer