class Solution(object):
    def lemonadeChange(self, bills):
        """
        time: O(n)
        space: O(1)
        :type bills: List[int]
        :rtype: bool
        """
        
        
        changes = {5:0, 10:0}
        
        for bill in bills: 
            if bill == 5: 
                changes[5] += 1
            elif bill == 10: 
                changes[10] += 1
                if changes[5] <= 0: 
                    return False
                else: 
                    changes[5] -= 1
            else:
                if changes[10] > 0 and changes[5] > 0: 
                    changes[10] -= 1
                    changes[5] -= 1
                elif changes[5] >= 3: 
                    changes[5] -= 3
                else: 
                    return False
        return True 
