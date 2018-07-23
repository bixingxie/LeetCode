class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        time: O(n)
        space: O(1)
        :type arr: List[int]
        :rtype: int
        """
        res = 0
        curMax = -1    
        for ind, val in enumerate(arr): 
            curMax = max(curMax, val)
            if curMax == ind:
                res += 1
        return res
