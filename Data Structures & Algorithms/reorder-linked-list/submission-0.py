import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 1
        cnt = head
        first = head
        sec = head

        while cnt.next:
            length += 1
            cnt = cnt.next
        
        mid = (length + 1) //2 

        for i in range(mid - 1):
            sec = sec.next
        
        temp = sec.next
        sec.next = None
        sec = temp

        def rev(node):
            curr = node
            prev = None

            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        
        second = rev(sec)

        while second:
            temp = first.next
            first.next = second
            second = second.next
            first.next.next = temp
            first = temp
        
        

        

        