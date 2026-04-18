# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        #find the middle of the linked list
        slow = fast = head
        while fast and fast.next:
            slow= slow.next
            fast = fast.next.next

        #reverse the second half
        prev, curr = None,slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        #merge first and reversed second halfs
        first, second = head, prev
        while second.next:
            first.next,first = second,first.next
            second.next,second = first,second.next
        
        