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
        if head != None:
            nodes = []
            while node:
                nodes.append(node.val)
                node = node.next
            result = ListNode(nodes[len(nodes) - 1])
            node = result
            index = len(nodes) - 2
            while index >= 0:
                node.next = ListNode(nodes[index])
                node = node.next
                index -= 1
            return result
        else:
            return head

        