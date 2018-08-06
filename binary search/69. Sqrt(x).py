class Solution:
    def mySqrt(self, x):
        """
        time: O(log(n))
        space: O(1)
        :type x: int
        :rtype: int
        """
        
        r = x + 1
        while r*r > x:
            r = int((r + x/r) / 2)
        return r
