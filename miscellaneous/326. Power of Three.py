class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        a = 1 
        while a < n: 
            a *= 3 
        return a == n 
