# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#to detect a cycle with a linked list, we can use two pointer
#slow pointer moves one node at a time, fast pointer moves two nodes at a time.
#if the two pointer meets, then return true

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True

        return False