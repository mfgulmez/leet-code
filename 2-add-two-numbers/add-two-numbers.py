

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        list1 = []
        list2 = []

        current_l1 = l1
        while current_l1 != None:
            list1.insert(0, current_l1.val)
            current_l1 = current_l1.next

        current_l2 = l2
        while current_l2 != None:
            list2.insert(0, current_l2.val)
            current_l2 = current_l2.next
        length1 = len(list1)
        length2 = len(list2)
        num1, num2 = 0, 0
        for i in range(len(list1)):
            num1 += list1[i] * pow(10, length1 - i - 1)
        
        for i in range(len(list2)):
            num2 += list2[i] * pow(10, length2 - i - 1)
        result = (num1 + num2)
        temp_result = result
        list_result = []
        while result >= 1:
            digit = result % 10
            list_result.append(digit)
            result = int(result / 10)
        l_result = ListNode()
        node = l_result
        for i in list_result:
            node.next = ListNode(i)
            node = node.next
 
        if(temp_result == 0):
            return l_result
        return l_result.next
        

            


        