## Problem:

Merge two sorted linked lists and return it as a sorted list.
The list should be made by splicing together the nodes of the first two lists.

`Example 1:`
`Input: l1 = [1,2,4], l2 = [1,3,4]`
`Output: [1,1,2,3,4,4]`

`Example 2:`
`Input: l1 = [], l2 = []`
`Output: []`

`Example 3:`
`Input: l1 = [], l2 = [0]`
`Output: [0]`

## Solution:

1. **Brute Force**
    1. As we are supposed to do it in place, there is only one solution. However, disregarding that condition of the problem, the most basic approach is using a third linked list `O(n) + O(m) space`, where `m` and `n` are the lengths of 2 input lists.
    2. p1 pointer on list 1, and p2 on list 2.
    3. Compare p1 with p2, add the value which is smaller to list 3 and increment corresponding pointer. Return list 3 at the end.
    > `O(m+n) time and space`

- **in place approach**
    1. Handle base conditions and always ensure to avoid null pointer exceptions (NPE) when it comes to linked lists.
    2. **Basic idea is to slide/push every value of one list inside the other list until we reach the end**
    3. Consider h1 as head pointer for list 1 and h2 for list 2. Start with the pointer which has a smaller value.
    4.  Loop till either h1 or h2 reaches the end:
        1. if h1.next.value ≤ h2.value: store temp1 = h1 and increment h1 → this adds link to previous node
        2. if h1.next.value > h2.value:
            1. store h2.next in temp2 respectively → this adds link to next node
            2. temp1.next = h2 and h2.next = h1 → slide h2 between temp1 which is previous node and this node h1
            3. h2 = temp2 → as we are looping, we have to bring h2 to the next value to be compared
    > `O(m+n) time and O(1) space -> as we have not used anything other than temp1 and temp2 which is constant space`
