class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #optimized, using zip and set
        
        if len(strs) == 0:
            return ''
        for index, value in enumerate(zip(*strs)): 
            if len(set(value)) != 1: 
                return strs[0][:index]
        return min(strs)
        
        
        
#         if len(strs) == 0:
#             return ''
#         if len(strs) == 1:
#             return strs[0]
        
#         prefix = ''
#         index = 0 
#         first_elem = strs[0]
        
#         while index < len(first_elem):
#             for i in range(1, len(strs)):
#                 try:
#                     if strs[i][index] != first_elem[index]:
#                         return prefix
#                 except IndexError:
#                     return prefix 
#             prefix += first_elem[index]
#             index += 1
        
#         return prefix
        
        
