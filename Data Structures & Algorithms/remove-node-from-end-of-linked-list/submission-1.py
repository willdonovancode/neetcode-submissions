# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter=1

        ans=head

        if head.next==None:
            return None

        prev=head
        fast=head.next

        while fast!=None:
            counter+=1
            fast=fast.next

        #head of list needs to be removed
        if counter==n:
            return head.next

        i=0
        while i < (counter-n)-1:
            i+=1
            prev=prev.next
        
        if prev.next.next==None:
            prev.next=None
            return ans
        
        nextNode=prev.next.next
        deleteNode=prev.next
        prev.next=nextNode
        deleteNode.next=None

        return ans
        
