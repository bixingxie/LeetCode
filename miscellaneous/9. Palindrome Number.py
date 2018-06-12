class Solution:
    def isPalindrome(self, x):
        """
        time: O(n)
        space: O(1)
        :type x: int
        :rtype: bool
        """
        
        #not converting to string, 50%
        if x < 0:
            return False 
        
        val = x 
        rev = 0
        
        while x > 0: 
            rev = rev * 10 + x % 10 
            x //= 10
        
        return val == rev
        
        
        #one liner 
        # return str(x) == str(x)[::-1]
    
        #not optimized and used string, 53%
#         x = str(x)
#         if(len(x) == 0):
#             return False 
#         elif(len(x) == 1):
#             return True
        
#         start = 0 
#         end = len(x)-1
        
#         while start < end:
#             if x[start] == x[end]:
#                 start += 1
#                 end -= 1
#             else: 
#                 return False 
        
#         return True
        
