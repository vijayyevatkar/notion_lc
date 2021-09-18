# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # return self.twoPass(head,n)
        return self.onePass(head,n)

    def onePass(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        firstNode = head
        secondNode = head
        prevNode = None

        for i in range(n):
            firstNode = firstNode.next
        
        while firstNode:
            prevNode = secondNode
            secondNode = secondNode.next
            firstNode = firstNode.next
        
        if not prevNode:
            return head.next
        prevNode.next = secondNode.next
        return head

    def twoPass(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = self.findLength(head)
        n2 = l-n
        i = 0
        traversalNode = head
        prevNode = None
        while traversalNode:
            if i == n2:
                break
            prevNode = traversalNode
            traversalNode = traversalNode.next
            i+=1
        if not prevNode:
            return traversalNode.next
        prevNode.next = traversalNode.next
        return head
            
    def findLength(self, head: Optional[ListNode]) -> int:
        traversalNode = head
        answer = 0
        while traversalNode:
            traversalNode = traversalNode.next
            answer += 1
        return answer    
        