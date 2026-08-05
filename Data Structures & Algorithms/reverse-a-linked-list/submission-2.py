# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        prev=None

        node=head

        while node:
            siguente=node.next
            node.next= prev # point backwards
            prev=node
            node=siguente
        
        return prev

