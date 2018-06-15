class Solution:
    def maxDistToClosest(self, seats):
        """
        time: O(n)
        space: O(1)
        :type seats: List[int]
        :rtype: int
        """
        
        res = i = 0 
        for index, val in enumerate(seats): 
            if val == 1: 
                res = i = index
                break
        j = i 
        i += 1
        while i < len(seats): 
            if seats[i] == 1: 
                res = max(res, (i-j) // 2)
                j = i 
            i += 1
        return max(res, len(seats) - j - 1)
    
