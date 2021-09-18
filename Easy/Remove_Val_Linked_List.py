# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        prevNode = None
        traversalNode = head

        while traversalNode:
            if traversalNode.val == val:
                if not prevNode:
                    head = head.next
                    traversalNode = head
                else:
                    traversalNode = traversalNode.next
                    prevNode.next = traversalNode
            else:
                prevNode = traversalNode
                traversalNode = traversalNode.next

        return head
