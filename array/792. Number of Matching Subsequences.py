import collections

class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        time: O(n**2)
        space: O(n), n = length of S
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        
        def isSubseq(d, word): 
            i = j = 0
            while i < len(word): 
                if word[i] not in d: 
                    return False
                flag = False 
                for ind in d[word[i]]: 
                    if ind >= j: 
                        j = ind + 1
                        flag = True
                        break 
                if not flag: 
                    return False 
                i += 1
            return True

        d = collections.defaultdict(list)
        for i in range(len(S)): 
            d[S[i]].append(i)
        return sum(isSubseq(d, word) for word in words)
