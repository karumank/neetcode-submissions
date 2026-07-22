class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}

        left = 0
        max_frequency = 0
        max_length = 0

        for right in range(len(s)):
            character = s[right]
            counts[character] = counts.get(character, 0) + 1

            max_frequency = max(max_frequency, counts[character])
            window_length = right - left + 1
            while window_length - max_frequency > k:
                counts[s[left]] -= 1
                left += 1
                window_length = right - left + 1
            

            max_length = max(max_length, window_length)
        return max_length

        