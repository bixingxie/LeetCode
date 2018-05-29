class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #optimized, 85%
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        res = 0 
        
        for char in s: 
            res += d[char]
            
        if s.find("IV") != -1: 
            res -= 2
        if s.find("IX") != -1:
            res -= 2
        if s.find("XL") != -1:
            res -= 20
        if s.find("XC") != -1:
            res -= 20 
        if s.find("CD") != -1:
            res -= 200
        if s.find("CM") != -1:
            res -= 200
            
        return res
    
#         index = len(s)-1
#         res = 0 
        
#         while index >= 0: 
#             currVal = d[s[index]]
#             if index-1 >= 0:
#                 preVal = d[s[index-1]]
#                 if currVal > preVal:
#                     res = res + currVal - preVal
#                     index -= 2
#                 else: 
#                     res += currVal
#                     index -= 1
#             else: 
#                 res += currVal
#                 index -= 1
                
#         return res
