"""Problem 2 - Add Two Numbers
   Link - https://leetcode.com/problems/add-two-numbers/description/
   Question - You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
              You may assume the two numbers do not contain any leading zero, except the number 0 itself."""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode()
        res = dummy
        carry = 0
        result = 0

        while l1 or l2 or carry:
            result = carry

            if l1:
                result+=l1.val
                l1 = l1.next
            if l2:
                result += l2.val
                l2 = l2.next
            
            num = result%10
            carry = result//10

            dummy.next = ListNode(num)
            dummy = dummy.next

        return res.next

        