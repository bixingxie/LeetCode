class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        time: O(n)
        space: O(1)
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(cost) > sum(gas): return -1
        tank = 0
        min_val, min_pos = 0, None
        for i in range(len(gas)): 
            tank = tank + gas[i] - cost[i]
            if tank < min_val: 
                min_val = tank 
                min_pos = i
        
        if min_pos == None: 
            return 0 
        else:
            return (min_pos + 1) % len(gas)
