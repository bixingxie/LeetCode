class Solution:
    
    #Alternative: dp
    def __init__(self):
        self.size = 0 
        self.start = 0
    
    """
    :type s: str
    :rtype: str
    """
    def longestPalindrome(self, s):
        
        for index in range(len(s)):
            self.checkOddPalindrome(s, index)
            self.checkEvenPalindrome(s, index)
            
        return s[self.start : self.start+self.size+1]
            
            
    def checkOddPalindrome(self, s, index): 
        start = index
        end = index 
        
        while (start >= 1 and end <= len(s)-2 and s[start-1] == s[end+1]):
            start -= 1
            end += 1 
        
        if(end-start) > self.size:
            self.size = end-start 
            self.start = start 
    
    def checkEvenPalindrome(self, s, index): 
        start = index 
        end = min(index+1, len(s)-1)
        
        while (start >= 1 and end <= len(s)-2 and s[start-1] == s[end+1] and s[start] == s[end]):
            start -= 1
            end += 1
            
        if(end-start) > self.size and s[start] == s[end]: 
            self.size = end-start 
            self.start = start
