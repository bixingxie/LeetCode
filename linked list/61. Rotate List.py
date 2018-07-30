# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        time: O(n)
        space: O(n)
        space complexity not optimized 
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if head == None or head.next == None: return head
        lst = [] 
        while head: 
            lst.append(head.val)
            head = head.next
        k %= len(lst)
        lst = lst[len(lst)-k:] + lst[:len(lst)-k]
        
        temp = newHead = ListNode(lst[0])
        
        for i in range(1, len(lst)): 
            temp.next = ListNode(lst[i])
            temp = temp.next
            
        return newHead
