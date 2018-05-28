class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
                #bruteforce not optimized
#         global_max = 0
        
#         for i in range(len(s)):
#             local_max = 0
#             local_d = {}
#             for j in range(i, len(s)):  
#                 if s[j] not in local_d:
#                     local_max += 1
#                     local_d[s[j]] = None
#                 else:
#                     break
                    
#                 if local_max > global_max: 
#                     global_max = local_max 
                
#         return global_max
    
        #optimized using hashtable and one forward pointer


        d = {}
        pointer = 0 
        max_val = 0
        
        for index, value in enumerate(s): 
            if value in d: 
                pointer = max(pointer, d[value]+1)
            max_val = max(max_val, index-pointer+1)
            d[value] = index
            
        return max_val
