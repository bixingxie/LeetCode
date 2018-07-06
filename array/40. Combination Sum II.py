class Solution:
    def combinationSum2(self, candidates, target):
        """
        time: 
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res
        
        
    def dfs(self, candidates, target, index, path, res): 
        if target < 0: 
            return 
        elif target == 0:
            res.append(path)
            return
        for j in range(index, len(candidates)): 
            if j != index and candidates[j] == candidates[j - 1]:
                continue
            self.dfs(candidates, target-candidates[j], j + 1, path + [candidates[j]], res)
