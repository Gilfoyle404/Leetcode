"""Problem 3 - Linked List Cycle
   Link - https://leetcode.com/problems/linked-list-cycle/description/?envType=problem-list-v2&envId=w1thoc57
   
   Question - Given head, the head of a linked list, determine if the linked list has a cycle in it.
   There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
   Return true if there is a cycle in the linked list. Otherwise, return false."""

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ptr1 = head
        ptr2 = head

        while ptr1 and ptr1.next:
            ptr1 = ptr1.next.next
            ptr2 = ptr2.next

            if ptr1 == ptr2:
                return True
        return False
        