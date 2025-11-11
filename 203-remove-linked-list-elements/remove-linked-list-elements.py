# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        node = head
        if head != None and head.val == val:
            while head != None and head.val == val:
                print("head")
                head = head.next
            node = head 
        
        while node != None:
            prev = node
            node = node.next
            if node != None and node.val == val:
                while node != None and node.val == val:
                    node = node.next
                prev.next = node
        return head