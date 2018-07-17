class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """

        res = [None] * len(A)
        A = collections.deque(sorted(A))
        B = collections.deque(sorted([(B[i], i) for i in range(len(B))]))
        while A and B: 
            a = A.popleft()
            b, index = B.popleft()
            
            if a > b: 
                res[index] = a
            else: 
                B.appendleft((b, index))
                last = B.pop()[1]
                res[last] = a 
        return res
