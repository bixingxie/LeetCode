class Solution:
    """
    My first solution, not optimized
    def convert(self, s, numRows):
        
        :type s: str
        :type numRows: int
        :rtype: str
        
        
        if(s == None or len(s) == 0):
            return ''
        if(numRows<=1):
            return s
        
        resList = [[] for i in range(numRows)]

        n = numRows*2-2
        counter = 0
        for index, value in enumerate(s): 
            if(counter > n): 
                counter %= n
            
            if(counter >= 0 and counter < numRows):
                resList[counter].append(value)
            else: 
                j = n - counter 
                resList[j].append(value)
                
            counter += 1
            
        return ''.join([str(item) for subList in resList for item in subList])

    """

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        #optimized: 97.81%
        
        if numRows == 1 or numRows >= len(s):
            return s
        
        res = [''] * numRows
        index = 0 
        step = 1
        
        for char in s: 
            res[index] += char 
            
            if(index == 0): 
                step = 1
            elif(index == numRows-1): 
                step = -1
                
            index += step
        
        return ''.join(res)
        
