# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        temp_node = head
        length_nodes = 0
        while temp_node:
            length_nodes += 1
            temp_node = temp_node.next
        if length_nodes == 0:
            return None
        k = k % length_nodes
        for i in range(k):
            temp_node = head
            temp_val = head.val
            while temp_node:
                if temp_node.next:
                    temp_next_val = temp_node.next.val
                    temp_node.next.val = temp_val
                    temp_val = temp_next_val
                else:
                    head.val = temp_val
                temp_node = temp_node.next
     
        return head