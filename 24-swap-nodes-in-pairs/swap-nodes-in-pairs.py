# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, listNode):
        node = listNode
        previousNode = None
        count = 0
        while node:
            if count % 2 == 0:
                if node.next:
                    midNode = node.next
                    nextNode = node.next.next
                    node.next = nextNode
                    midNode.next = node
                    if previousNode:
                        previousNode.next = midNode
                    else:
                        listNode = midNode
                    node = midNode
            previousNode = node
            node = node.next
            count += 1
        return listNode

    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        return self.swapNodes(head)