class Solution:
    def divide(self, dividend, divisor):
        """
        time = O(log(n))
        space = O(1)
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0: 
            sign = -1
        else:
            sign = 1
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            shift = 0
            while (divisor << shift) <= dividend:
                shift += 1
            dividend -= (divisor << shift-1)
            res += (1 << shift-1)
        return min(max(-2147483648, res*sign), 2147483647)
        
