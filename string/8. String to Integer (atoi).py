class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        #optimized, 99%
        
        sign = 1
        res = 0
        
        str = str.strip()
        if len(str) == 0: 
            return 0
        if str[0] == '+': 
            sign = 1
            str = str[1:]
        elif str[0] == '-': 
            sign = -1
            str = str[1:]
            
        for char in str: 
            if char.isdigit(): 
                res = res*10 + int(char)
            else:
                break
                
        res*=sign
        
        if res > 2**31-1 :
            return 2**31-1
        elif res < -2**31:
            return -2**31
        else:
            return res
