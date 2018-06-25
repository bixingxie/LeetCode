class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        time: O(n)
        space: O(1)
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        res = len(words)-1 
        a = b = -1 
        for i in range(len(words)): 
            if words[i] == word1: 
                a = i 
            elif words[i] == word2:
                b = i 
            if a != -1 and b != -1: 
                res = min(res, abs(a - b))
        return res
