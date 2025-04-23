from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        current = dummy_head

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            total = v1 + v2 + carry
            carry = total // 10
            val = total % 10
            current.next = ListNode(val)

            # update pointer
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy_head.next


l1 = [2, 4, 3]
l2 = [5, 6, 4]
# Linked list
dummy = ListNode(0)
current = dummy
for i in l1:
    current.next = ListNode(i)
    current = current.next
linkedList_l1 = dummy.next

dummy = ListNode(0)
current = dummy
for i in l2:
    current.next = ListNode(i)
    current = current.next
linkedList_l2 = dummy.next

s = Solution()
print(s.addTwoNumbers(linkedList_l1, linkedList_l2).val)
