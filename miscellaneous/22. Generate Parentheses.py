class Solution:
    def generateParenthesis(self, n):
        """
        time: O(n!) - Catalan Numbers: 
        space: O(n)
        :type n: int
        :rtype: List[str]
        n=2: ()(), (())
        n=3:
        """
        
        res = []
        if n == 0: return res
        self.generate(res, '', n, n)
        return res
    
    def generate(self, res, string, left, right): 
        if left > right: 
            return 
        if right == 0 and left == 0: 
            res.append(string)
            return 
        if left > 0: 
            self.generate(res, string + '(', left - 1, right)
        if right > 0: 
            self.generate(res, string + ')', left, right - 1)
            
                    
        
