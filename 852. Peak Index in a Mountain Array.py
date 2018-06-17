class Solution:
    def peakIndexInMountainArray(self, A):
        """
        time: O(n)
        space: O(1)
        :type A: List[int]
        :rtype: int
        """
        
        for index, val in enumerate(A): 
            if index + 1 < len(A) and val > A[index+1]:
                return index 
        return None
