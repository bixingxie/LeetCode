# Definition for singly-linked list.

class Solution:
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # count the remaining nodes from k
        # if less than k, do not revese
        count = 0
        curr = head
        while curr and count < k:
            curr = curr.next
            count += 1
        if count < k:
            return head
        # Now we need to reverse the next k nodes
        prev = None
        curr = head
        for i in range(k):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        # now "head" is actually the tail of these reversed nodes
        # if there's more nodes left, recursively reverse them
        # and set the current group's tail("head")'s next to be the 
        # next group's head.
        if curr:
            head.next = self.reverseKGroup(curr, k)
        return prev
