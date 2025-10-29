# Definition for singly-linked list.
#class ListNode(object):
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 == None and list2 == None:
            return None
        result = ListNode()
        body = result
        
        while list1 != None and list2 != None:
            print(list1.val, list2.val)
            if list1.val > list2.val:
                body.val = list2.val
                body.next = ListNode()
                body = body.next
                list2 = list2.next
            
            elif list2.val > list1.val:
                body.val = list1.val
                body.next = ListNode()
                body = body.next
                list1 = list1.next

            else:
                body.val = list1.val
                body.next = ListNode()
                body = body.next
                list1 = list1.next

                body.val = list2.val
                body.next = ListNode()
                body = body.next
                list2 = list2.next     

        while list1 != None:
            body.val = list1.val 
            body.next = ListNode()
            body = body.next
            list1 = list1.next

        while list2 != None:
            body.val = list2.val 
            body.next = ListNode()
            body = body.next
            list2 = list2.next
        body = result
        while body.next.next != None:
            print(body.val)
            body = body.next
        body.next = None
        return result      

            

        