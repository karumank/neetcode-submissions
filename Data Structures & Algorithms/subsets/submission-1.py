from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Result array
        result = []

        def dfs(index, temp_array):
            result.append(temp_array.copy())

            while index < len(nums):
                temp_array.append(nums[index])
                dfs(index + 1, temp_array)
                temp_array.pop()
                index += 1

        dfs(0, [])
        
        return result