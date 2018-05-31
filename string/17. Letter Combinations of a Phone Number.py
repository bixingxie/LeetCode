class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        d = {'0':' ',
             '1':'*',
             '2':"abc", 
             '3':"def",
             '4':"ghi",
             '5':"jkl",
             '6':"mno",
             '7':"pqrs",
             '8':"tuv",
             '9':"wxyz"}
        
        if digits == "":
            return []

        results = []
        
        for digit in digits: 
            if len(results) == 0: 
                for char in d[digit]: 
                    results.append(char) 
            else:
                tempResults = []
                for result in results:
                    for letter in d[digit]:
                        tempResults.append(result + letter)
                results = tempResults
        return results
                    
