class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer than s2, no permutation can exist.
        if len(s1) > len(s2):
            return False

        # Store character counts of s1 and the current window.
        target = {}
        window = {}

        # Build the frequency map for s1.
        for character in s1:
            target[character] = target.get(character, 0) + 1

        left = 0

        # Expand the sliding window across s2.
        for right in range(len(s2)):
            character = s2[right]
            window[character] = window.get(character, 0) + 1

            # Keep the window size equal to len(s1).
            if right - left + 1 > len(s1):
                left_character = s2[left]
                window[left_character] -= 1

                # Remove zero-count entries.
                if window[left_character] == 0:
                    del window[left_character]

                left += 1

            # Compare frequency maps.
            if window == target:
                return True

        return False