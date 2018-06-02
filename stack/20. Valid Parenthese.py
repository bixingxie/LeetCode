class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if(len(s) % 2) != 0: return False
        d = {')':'(', ']':'[', '}':'{'}
        stack = []
        for char in s: 
            if char == '(' or char == '[' or char == '{': 
                stack.append(char)
            else: 
                if len(stack) == 0:
                    return False 
                par = stack.pop()
                try:
                    if par != d[char]:
                        return False 
                except KeyError: 
                    return False
        return len(stack) == 0
