# Case - Given n numbers (n = 3, 1,2,3], return all combinations of K length say 2
# Key: We will not reuse numbers as we want all combinations like 1,2 1,3, 2,3 etc


def combine(self, n: int, k: int) -> List[List[int]]:
        
        self.result = []
        self.k = k
        if not k:
            return self.result
        
        self.helper(1, n+1, [])
        return self.result
    
    
    
    def helper(self, first, n, current):
        
        # base case, only constraint where we need to take a snapshot and return to rec call function is based on length
        if len(current) == self.k:
            self.result.append(current.copy())
        
        
        #logic
        
        for i in range(first, n):
            current.append(i)
            self.helper(i+1, n, current) # i+1 as we want other combinations
            
            current.pop()
