# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        curr = head
        visited = {curr : 1}
        while curr:
            if not visited.get(curr.next):
                visited[curr.next] = 1
            else:
                return True
            curr = curr.next
        return False
        