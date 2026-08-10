# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        v=set()
        start=head
        while start is not None:
            if start in v:
                return True
            v.add(start)
            start=start.next
        return False