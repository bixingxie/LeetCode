class Solution:
    def hIndex(self, citations):
        """
        time: O(log(n))
        space: O(1)
        :type citations: List[int]
        :rtype: int
        """

        low, high = 0, len(citations)-1
        while low <= high: 
            mid = (low + high) // 2
            if citations[mid] < len(citations) - mid: 
                low = mid + 1
            else: 
                high = mid - 1
        return len(citations) - low
