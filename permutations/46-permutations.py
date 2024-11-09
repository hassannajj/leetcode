class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result, temp = [], []

        def backtrack():
            # base case
            if len(temp) == n:
                result.append(temp[:])
            
            for x in nums:
                if x not in temp:
                    temp.append(x)
                    backtrack()
                    temp.pop()
    
            

        
        backtrack()
        return result


