class Solution(object):
    def countAndSay(self, n):
        """
        time: O(n*3)
        space: O(n)
        :type n: int
        :rtype: str
        """
        
        if n < 1: 
            return ''
        elif n == 1: 
            return '1'
        else: 
            prev = self.countAndSay(n - 1)
            res = ''
            count = 1
            for i in range(len(prev) - 1): 
                if prev[i] == prev[i + 1]: 
                    count += 1
                else:
                    res = res + str(count) + prev[i]
                    count = 1 
            res = res + str(count) + prev[-1]
            return res
                
