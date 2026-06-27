# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Remember, you cannot make prev a dummy node, it will create infinite loop
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev
        