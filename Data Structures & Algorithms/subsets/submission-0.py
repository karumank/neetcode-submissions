class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        def dfs(idx):
            if idx == len(nums):
                result.append(path.copy())
                return 
            path.append(nums[idx])
            dfs(idx + 1)
            path.pop()
            dfs(idx + 1)
        
        dfs(0)
        return result