class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set()

        for num in nums:
            nums_set.add(num)
    
        visited_set = set()
        result = 0
        for num in nums:
            curr_len = 1
            if num not in visited_set:
                visited_set.add(num)
                curr_num = num + 1
                while curr_num in nums_set: 
                    curr_len += 1
                    visited_set.add(curr_num)
                    curr_num += 1
                    
            result = max(curr_len, result)
        return result

