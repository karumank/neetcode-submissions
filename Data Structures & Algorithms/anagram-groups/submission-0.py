class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for curr_str in strs:
            key = ''.join(sorted(curr_str))
            anagram_map[key].append(curr_str)
        return list(anagram_map.values())