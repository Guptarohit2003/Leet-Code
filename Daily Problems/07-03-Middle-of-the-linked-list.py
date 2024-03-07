from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


print(
    Solution()
    .middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
    .val
)  # 3
print(Solution.middleNode([1, 2, 3, 4, 5]))
