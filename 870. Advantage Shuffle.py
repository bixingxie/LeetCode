class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        
        res = []
        for i in range(len(B)): 
            local_min = float("inf")
            index = -1

            if B[i] > max(A):
                local_min = min(A)
                index = A.index(local_min)

            else:
                for j in range(len(A)):
                    if A[j] > B[i]: 

                        local_min = min(local_min, A[j])
                        if local_min == A[j]:
                            index = j 
    
            
            res.append(local_min)
            A.pop(index)
        return res

s = Solution()
print(s.advantageCount([2,7,11,15], [1,10,4,11]))

