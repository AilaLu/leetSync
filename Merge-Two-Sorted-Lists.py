# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #edge case is if either of the list is empty
    #create a variable head to point to the smaller start
    #use a current to iterate. with each iteration:
        #points to the smaller value and update current
    #return head
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1

        if list1.val <= list2.val: 
            head = cur = list1
            #update list1 or it will be stuck in a loop 
            list1 = list1.next
        else: 
            head = cur = list2
            list2 = list2.next

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else: 
                cur.next = list2
                list2 = list2.next
            # update cur or else line 25 and 28 will keep overwriting 
            cur = cur.next 

        # Append the remaining nodes
        cur.next = list1 if list1 else list2
        return head