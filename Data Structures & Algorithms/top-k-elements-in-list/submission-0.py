class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = {}
        for n in nums:
            if n in nums_map:
                nums_map[n] += 1
            else:
                nums_map[n] = 1
        freq_bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in nums_map.items():
            freq_bucket[freq].append(num)
        res = []
        for i in reversed(range(len(freq_bucket))):
            item = freq_bucket[i]
            for num in item:
                res.append(num)
                k -= 1
                if k == 0:
                    return res

        return res


        