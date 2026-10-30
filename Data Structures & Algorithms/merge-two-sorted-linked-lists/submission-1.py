# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        mh = ListNode()
        if l1 is None:
            mh = l2
            return mh
        if l2 is None :
            mh = l1
            return mh
        
        if l1.val <= l2.val:
            mh = l1
            l1 = l1.next
            mh.next = None
        else:
            mh=l2
            l2=l2.next
            mh.next = None

        curr = mh
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
                curr.next.next = None
                curr = curr.next

            else:
                curr.next = l2
                l2 = l2.next
                curr.next.next = None
                curr = curr.next
        if l1 is None:
            curr.next = l2
        if l2 is None :
            curr.next = l1
        return mh



        
        
        


        