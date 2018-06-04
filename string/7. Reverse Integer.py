class Solution:
    def reverse(self, x):
        """
        time: O(n)
        :type x: int
        :rtype: int
        
        
        #Version 1: 87%
        sign = [1, -1][x<0]
        x = abs(x)
        y = 1
        count = 0
        sum = 0
        
        for index in range(len(str(x))): 
            sum += int(str(x)[index]) * y 
            y *= 10 
            count += 1
            
        if sum >= 2**31:
            return 0
        else: 
            return sum * sign
        """

        #Version 2: 97%
        sign = [1, -1][x<0]
        res = int(str(abs(x))[::-1])
        if res >= 2**31:
            return 0
        else: 
            return res*sign
