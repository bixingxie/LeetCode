class Solution:
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        second = head.next 
        head.next = self.swapPairs(second.next)
        second.next = head
        return second
