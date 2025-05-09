# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    \\\
    1. create a prev node with value null
    2. with a while loop, while the node is not null, means cur exist
        1. create a variable that store the original cur.next value
        2. cur points to prev
        3. prev moves on to cur
        4. cur moves on to the original cur.next

    the edge case where head is [] will cause Attribute error if use cur.cal as the condition for while loop 
    \\\
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        cur = head

        while cur: 
            og_next = cur.next
            cur.next = prev
            prev = cur
            cur = og_next
        
        return prev
