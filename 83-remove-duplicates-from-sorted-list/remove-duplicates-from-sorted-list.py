# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head == None:
            return None
        temp = head
        value = head.val
        
        while temp != None:
            if temp.next != None:
                while value == temp.next.val:
                    if value == temp.next.val:
                        end = temp.next.next
                        if end != None:
                            temp.next = end

                        else:
                            temp.next = None
                            return head
                        
                else:
                    value = temp.next.val
            temp = temp.next
        return head