#method1: conversion to a list
class Solution:
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None
        
    def mergeKLists(self, lists):
        """
        time: O(nlogk), k is the number of list in lists
        space: O(n)
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        lst = [] 
        for head in lists: 
            while head: 
                lst.append(head.val)
                head = head.next 
        lst.sort()
        res = ListNode(0)
        ptr = res
        for num in lst: 
            ptr.next = ListNode(num)
            ptr = ptr.next 
        return res.next


#method2: mergeSort
class Solution:
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None
    
    def mergeTwoLists(self, list1, list2):
        """
        time: O(nlogn)
        space: O(n)
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ptr = res = ListNode(0)
        while list1 and list2: 
            if list1.val <= list2.val: 
                ptr.next = list1
                list1 = list1.next 
            else:
                ptr.next = list2
                list2 = list2.next
            ptr = ptr.next
        if not list1: 
            ptr.next = list2
        else:
            ptr.next = list1
        return res.next 
        
    def mergeKLists(self, lists):
        """
        time: O(nlogn)
        space: O(n)
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0: 
            return 
        res = []
        for lst in lists:
            res.append(lst)
        while len(res) > 1: 
            l1 = res.pop()
            l2 = res.pop()
            res.append(self.mergeTwoLists(l1, l2))
        return res[0]
            
