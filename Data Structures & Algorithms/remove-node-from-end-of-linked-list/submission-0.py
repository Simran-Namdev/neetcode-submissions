# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        cnt = head
        while cnt.next:
            cnt = cnt.next
            l += 1
        
        node = l - n 

        if node == -1:
            return head.next

        curr = head
        for _ in range(node):
            curr = curr.next
        
        temp = curr.next
        curr.next = curr.next.next
        temp.next = None
    
        return head



        