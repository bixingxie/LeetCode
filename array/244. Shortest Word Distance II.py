from collections import defaultdict
class WordDistance:

    def __init__(self, words):
        """
        time: O(n)
        space: O(n)
        :type words: List[str]
        """
        self.l = len(words)
        self.d = defaultdict(list)
        for index, val in enumerate(words): 
            self.d[val].append(index)
                
    def shortest(self, word1, word2):
        """
        time: O(n)
        space: O(n)
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        diff = float("inf")
        lst1, lst2 = self.d[word1], self.d[word2]
        i = j = 0
        while i < len(lst1) and j < len(lst2): 
            diff = min(diff, abs(lst1[i] - lst2[j]))
            if lst1[i] > lst2[j]:
                j += 1
            else:
                i += 1
        return diff


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
