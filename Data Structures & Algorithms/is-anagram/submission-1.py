class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = {}
        if len(s) != len(t):
            return False
            
        for c in s:
            if c in char_count:
                char_count[c] += 1
            else:
                char_count[c] = 1
        
        for c in t:
            if c in char_count:
                char_count[c] -= 1
                if char_count[c] == 0:
                    char_count.pop(c)
            else:
                False
        
        return len(char_count) == 0