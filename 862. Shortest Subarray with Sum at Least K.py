class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        
        sub_len = float("inf")
        for index, val in enumerate(A):
            if val >= K:
                return 1
            j = index + 1
            jSum = val 
            while j < len(A):
                jSum += A[j]
                if jSum >= K:
                    sub_len = min(sub_len, j - index + 1)
                    break
                j += 1
        if sub_len == float("inf"):
            return -1
        else:
            return sub_len
        
s = Solution()
print(s.shortestSubarray([2,-1,2], 3))
