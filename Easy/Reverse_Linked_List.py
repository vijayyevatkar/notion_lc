# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prevNode = None
        traversalNode = head
        nextNode = None
        
        while traversalNode:
            nextNode = traversalNode.next
            traversalNode.next = prevNode
            prevNode = traversalNode
            traversalNode = nextNode
            
        return prevNode