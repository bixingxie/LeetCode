class Solution:
    def hIndex(self, citations):
        """
        time: O(nlogn)
        space: O(1)
        :type citations: List[int]
        :rtype: int
        """
        
        if len(citations) == 0: return 0
        citations.sort()
        citations = citations[::-1]
        for i in range(len(citations)): 
            if citations[i] < i+1: 
                return i 
        return len(citations)
        
