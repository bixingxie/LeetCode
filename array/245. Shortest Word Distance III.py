class Solution:
    def shortestWordDistance(self, words, word1, word2):
        """
        time: O(n)
        space: O(1)
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        res = len(words) - 1 
        a = b = -1
        for index, val in enumerate(words): 
            if val == word1:
                a = index 
                if b != -1 and a != b: 
                    res = min(res, abs(a - b))
            if val == word2:
                b = index 
                if a != -1 and a != b: 
                    res = min(res, abs(a - b))
        return res
