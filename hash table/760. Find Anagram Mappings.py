class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        
        if not A or not B: return []

        res = []
        d = {}
        for index, elem in enumerate(B): 
            if elem not in d: 
                d[elem] = [index]
            else: 
                d[elem].append(index)
        
        for elem in A: 
            res.append(d[elem].pop())
        return res
