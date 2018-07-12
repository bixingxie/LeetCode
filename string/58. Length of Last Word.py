class Solution(object):
    def lengthOfLastWord(self, s):
        """
        time: O(n)
        space: O(1)
        :type s: str
        :rtype: int
        """
        
        if not s or len(s) == 0: return 0 
        res = 0
        j = len(s) - 1 
        flag = False
        while j >= 0: 
            if s[j] != ' ': 
                flag = True
                res += 1
            else:
                if flag == True:
                    break 
            j -= 1
        return res 
