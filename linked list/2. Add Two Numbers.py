class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        ret = ListNode(0)
        ptr = ret 
        carry = 0
        while l1 or l2 or carry:
            res = 0
            if l1:
                res += l1.val
                l1 = l1.next
            if l2:
                res += l2.val
                l2 = l2.next

            data = (res + carry) % 10 
            newNode = ListNode(data)
            carry = (res + carry) // 10

            ptr.next = newNode
            ptr = ptr.next

        return ret.next



        
            
