# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        #Handle all the base cases first
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        # answer points to the first node of the final list that we will return
        answer = None
        answer = l1 if l1.val <= l2.val else l2
        
        #important to initialize p1 as null
        p1 = None
        
        # iterate until we reach end of either one of the lists
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                # this means l1 is smaller, just store previous pointer and increment
                p1 = l1
                l1 = l1.next
            else:
                # this means l2 is smaller, meaning we have to push l2 between previous and current pointer
                temp2 = l2.next
                if p1 is not None:
                    # corner case, if at first comparison if l2 is less, l2 becomes the previous pointer.
                    p1.next = l2
                l2.next = l1
                p1 = l2
                l2 = temp2
        
        # at the end, if l2 is still remaining but l1 is over, attach l2 to p1
        if l1 is None and l2 is not None:
            p1.next = l2
        
        # in any other case where both are null or only l1 is pending, we can just return answer
        return answer


