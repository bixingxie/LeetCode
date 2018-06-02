# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        optimized by using a hashtable, 95%
        time: O(L)
        space: O(L)
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
    
        count = 0 
        curr = head 
        d = {}
        
        while curr:
            d[count] = curr
            count += 1
            curr = curr.next 
        if count == n: 
            return head.next 
        d[count-n-1].next = d[count-n-1].next.next
        return head
        
        
