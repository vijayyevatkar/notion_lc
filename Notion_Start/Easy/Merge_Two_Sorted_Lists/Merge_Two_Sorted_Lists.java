/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {

        // Check for all the base conditions:
        if ((null == l1) && (null==l2)) return null;
        if (null == l1) return l2;
        if (null == l2) return l1;

        // temp2 is the next node and p1 is the previous node
        ListNode answer,temp2,p1;

        // answer points to the first node of the final list that we will return
        if(l1.val <= l2.val) answer = l1;
        else answer = l2;

        //important to initialize p1 as null
        p1=null;
        //iterate until we reach end of either one of the lists
        while(l1 != null && l2 != null) {            
            if(l1.val <= l2.val) {
                // this means l1 is smaller, just store previous pointer and increment
                p1 = l1;
                l1 = l1.next;
            } else {
                // this means l2 is smaller, meaning we have to push l2 between previous and current pointer
                temp2 = l2.next;
                // corner case, if at first comparison if l2 is less, l2 becomes the previous pointer.
                if(p1 != null) p1.next = l2;
                l2.next = l1;
                p1 = l2;
                l2 = temp2;                
            }
        }

        // at the end, if l2 is still remaining but l1 is over, attach l2 to p1
        // in any other case where both are null or only l1 is pending, we can just return answer
        if ((l1 == null) && (l2 != null )) p1.next = l2;
        return answer;
    }
}