class Solution:
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    def mergeTwoLists(self, l1, l2):
        """
        time: O(n)
        space: O(n)
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        resList = ListNode(0)
        newList = resList

        while l1 and l2: 
            if l1.val <= l2.val: 
                newList.next = ListNode(l1.val)
                l1 = l1.next 
            else:
                newList.next = ListNode(l2.val)
                l2 = l2.next 
            newList = newList.next 
            
        while l1:
            newList.next = ListNode(l1.val)
            l1 = l1.next 
            newList = newList.next 
            
        while l2: 
            newList.next = ListNode(l2.val)
            l2 = l2.next 
            newList = newList.next 
            
        return resList.next
