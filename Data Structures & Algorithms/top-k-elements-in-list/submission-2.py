class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            if num not in freq_map:
                freq_map[num] = 0
            freq_map[num] += 1
        result = []
        for key, value in sorted(freq_map.items(), key=lambda item: item[1], reverse=True):
            result.append(key)
            if len(result) == k:
                break
        
        return result
    