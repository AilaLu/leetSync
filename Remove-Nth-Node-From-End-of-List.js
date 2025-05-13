/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */

//  using two pointer, both from the dummy before head
// keep the offset between slow and fast as n, so by the time fast reaches to the end, slow is at nth from the end
var removeNthFromEnd = function(head, n) {
    let dummy = new ListNode(0, head)
    let slow = dummy
    let fast = dummy
    // fast pointer has a head start and has the n distance with slow pointer
    for(let i = 0; i <= n; i++){
        fast = fast.next
    }

    // iterate until fast reaches to the end
    while(fast !== null){
        slow = slow.next
        fast = fast.next
    }

    // delete the nth node from the end by pointing slow to the next after next, which is skipping slow.next
    slow.next = slow.next.next
    return dummy.next
};