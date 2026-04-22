"""Problem 19 - Remove Nth Node From End of List
   Link - https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=problem-list-v2&envId=w1thoc57
   
   Question - Given the head of a linked list, remove the nth node from the end of the list and return its head."""
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        list1 = []
        while head:
            list1.append(head.val)
            head = head.next
        list1.pop(len(list1) - n)

        dummy = ListNode()
        result = dummy
        for num in list1:
            dummy.next = ListNode(num)
            dummy = dummy.next
        return result.next
        