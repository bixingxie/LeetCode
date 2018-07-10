class Solution:
    def myPow(self, x, n):
        """
        time: O(log(n))
        space: O(1)
        :type x: float
        :type n: int
        :rtype: float
        """
        
        if n == 1: return x
        elif n == 2: return x * x
        elif n == 0: return 1
        elif n < 0: return self.myPow(1/x, n*-1)
        else:
            res = self.myPow(x, n//2) 
            if n % 2 == 0:
                return res * res 
            else: 
                return res * res * x
