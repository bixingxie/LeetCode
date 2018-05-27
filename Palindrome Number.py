class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #not optimized and used string, 53%
        x = str(x)
        if(len(x) == 0):
            return False 
        elif(len(x) == 1):
            return True
        
        start = 0 
        end = len(x)-1
        
        while start < end:
            if x[start] == x[end]:
                start += 1
                end -= 1
            else: 
                return False 
        
        return True
        
