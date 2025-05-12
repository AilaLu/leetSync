# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# // detect cycles in a linked list - two pointer 
# // Slow Pointer: Moves one step at a time.
# // Fast Pointer: Moves two steps at a time.
# // If there is a cycle, the fast pointer will eventually meet the slow pointer. 
# // This is because the fast pointer, moving faster, will eventually \lap\ the slow pointer if the list contains a cycle.

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False