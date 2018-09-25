class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        res = mask = 0 
        for i in range(32)[::-1]:
            mask = mask | 1 << i 
            d = {}
            for num in nums: 
                d[num & mask] = None 
                
            #assume the ith bit from right to be 1 
            temp = res | 1 << i 
            for key in d: 
                if key ^ temp in d: 
                    res = temp 
        return res 
