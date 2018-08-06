class Solution:
    def addBinary(self, a, b):
        """
        time: O(n)
        space: O(n)
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) == 0: return b 
        if len(b) == 0: return a
        
        num = str(int(a) + int(b))
        i = len(num) - 1
        res = ''
        carry = 0 
        while i >= 0: 
            res = str((int(num[i]) + carry) % 2) + res  
            carry = (int(num[i]) + carry) // 2
            i -= 1

        if carry: return str(carry) + res
        else: return res
    
