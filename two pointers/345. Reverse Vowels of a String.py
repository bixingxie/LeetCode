class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if not s or len(s) == 0: return ''
        front, end = 0, len(s) - 1 
        res = list(s)
        
        d = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0, 'A':0, 'E':0, 'I':0, 'O':0, 'U':0}
        while front < end: 
            if s[front] not in d and s[end] not in d:
                front += 1
                end -= 1
            elif s[front] not in d: 
                front += 1 
            elif s[end] not in d: 
                end -= 1
            else: 
                res[front], res[end] = res[end], res[front]
                front += 1
                end -= 1
        return ''.join(res)
