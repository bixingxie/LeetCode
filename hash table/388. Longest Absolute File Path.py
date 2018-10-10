class Solution:
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        
        res, d = 0, {-1:0}
        
        for line in input.split("\n"): 
            depth = line.count("\t")
            d[depth] = d[depth-1] + len(line) - depth
            if line.count("."): 
                res = max(res, d[depth] + depth)
        return res
