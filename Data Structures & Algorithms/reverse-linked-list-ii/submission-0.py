# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev = None
        curr = head

        for i in range(left-1):
            prev = curr
            curr = curr.next
        
                # save connections
        left_prev = prev
        reverse_tail = curr

        # reverse sublist
        prev2 = None
        curr2 = curr

        for i in range(right - left + 1):
            temp = curr2.next
            curr2.next = prev2
            prev2 = curr2
            curr2 = temp

        # reconnect left side
        if left_prev:
            left_prev.next = prev2
        else:
            head = prev2

        # reconnect right side
        reverse_tail.next = curr2

        return head
