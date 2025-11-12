# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        nums = []

        while head != None:
            nums.append(head.val)
            head = head.next
        index = 0
        while index <= len(nums) // 2:
            if nums[index] != nums[len(nums) - index - 1]:
                return False
            index += 1
        return True