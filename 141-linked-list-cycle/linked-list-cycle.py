# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        turtle, rabbit = head, head

        while turtle != None and rabbit != None and rabbit.next != None:
            turtle = turtle.next
            rabbit = rabbit.next.next
            if turtle == rabbit:
                return True
        return False
        