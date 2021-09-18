# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        if head == None:
            return False
        
        first = head
        second = head.next

        while True:
            if first == None or second == None:
                return False
            if first == second:
                break
            first = first.next
            second = second.next
            if second == None:
                return False
            second = second.next
        
        return True