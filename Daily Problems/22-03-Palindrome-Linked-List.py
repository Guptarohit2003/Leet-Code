from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def _init_(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def check(l1, l2):
            while l1 and l2:
                if l1.val != l2.val:
                    return False
                l1 = l1.next
                l2 = l2.next
            return l1 == None and l2 == None

        fast, prev, slow = head, None, head
        while fast and fast.next:
            fast = fast.next.next
            nextt = slow.next
            slow.next = prev
            prev = slow
            slow = nextt
        return check(prev, slow) or check(prev, slow.next)
