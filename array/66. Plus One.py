class Solution(object):
    def plusOne(self, digits):
        """
        time: O(n)
        space: O(1)
        :type digits: List[int]
        :rtype: List[int]
        """
        
        i = len(digits) - 1
        carry = 0 
        digits[i] += 1
        while i >= 0: 
            digits[i] = digits[i] + carry 
            carry = digits[i] // 10 
            digits[i] %= 10 
            i -= 1
        if carry == 1: 
            digits.insert(0, 1)
        return digits
        
