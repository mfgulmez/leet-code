# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def sortLists(self, lists):
        nodes = [indexNode for indexNode in lists if indexNode]
        sortedLinkedList = ListNode()
        sortedIterator = sortedLinkedList
        if len(nodes) == 0:
            return None
        while nodes:
            min_index = 0
            for i in range(1, len(nodes)):
                if nodes[i].val < nodes[min_index].val:
                    min_index = i
           
            sortedIterator.val = nodes[min_index].val
            if nodes[min_index].next:
                nodes[min_index] = nodes[min_index].next
            else:
                nodes.pop(min_index)
            if nodes:
                sortedIterator.next = ListNode()
                sortedIterator = sortedIterator.next
        return sortedLinkedList    

    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        return self.sortLists(lists)
    