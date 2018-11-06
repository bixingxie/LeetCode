class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        
        d = {}
        for ind, email in enumerate(emails): 
            local, domain = email.split('@')
            local = local.replace('.', '')
            if '+' in local: 
                local = local[:local.find('+')]
            if domain not in d: 
                d[domain] = [local] 
            else: 
                if local not in d[domain]: 
                    d[domain].append(local)
                    
        res = 0 
        for key in d: 
            res += len(d[key])

        return res
s
