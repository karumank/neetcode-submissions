class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = set()

        left = 0
        max_length = 0

        for right in range(len(s)):

            while s[right] in characters:
                characters.remove(s[left])
                left += 1
            
            characters.add(s[right])

            current_length = right - left + 1

            max_length = max(current_length, max_length)
        
        return max_length
        