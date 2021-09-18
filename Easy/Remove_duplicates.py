# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        
        prevNode = head
        traversalNode = head.next
        
        while traversalNode:

            if prevNode.val == traversalNode.val:
                traversalNode = traversalNode.next
                prevNode.next = traversalNode
            else:
                prevNode = traversalNode
                traversalNode = traversalNode.next
        
        return head