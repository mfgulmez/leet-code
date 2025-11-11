# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        node = head
        result = ListNode()
        while node:
            if result.next:
                reverse_node = ListNode(node.val, result.next)
                result.next = reverse_node
            else:
                reverse_node = ListNode(node.val)
                result.next = reverse_node
            node = node.next
        
        result = result.next
        return result