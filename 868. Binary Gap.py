class Solution(object):
    def binaryGap(self, N):
        """
        time: O(n)
        space: O(n)
        :type N: int
        :rtype: int
        """
        
        
        binary = "{0:b}".format(N)
        res = temp = i = 0 
        while i < len(binary): 
            if binary[i] == '1': 
                res = max(res, temp)
                temp = 0 
            temp += 1
            i += 1
        return res
