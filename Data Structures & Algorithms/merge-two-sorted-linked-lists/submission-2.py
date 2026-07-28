#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def addNode(n1,head):
    temp=ListNode()
    temp.val=n1.val
    temp.next=None
    head.next=temp



class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 ==None:
            return list2
        if list2==None:
            return list1
        if list1 and list2 ==None:
            return []
        head=ListNode()
        temp=head
       
        while list1!= None and list2!=None:
            if list1.val<list2.val:
                addNode(list1,temp)
                list1=list1.next
                temp=temp.next
            else:
                addNode(list2,temp)
                list2=list2.next
                temp=temp.next
        if list1!=None:
            temp.next=list1
            temp=temp.next
        if list2!=None:
            temp.next=list2
            temp=temp.next

        return head.next