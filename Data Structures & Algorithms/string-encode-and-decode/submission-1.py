class Solution:

    def encode(self, strs: List[str]) -> str:
        result_str = []

        for curr_str in strs:
            str_len = len(curr_str)
            result_str.append(str(str_len) + "#"+ str(curr_str))
        
        return "".join(result_str)

# ["Hello", "World"]
# Encoded: "5#Hello5#World"

    def decode(self, s: str) -> List[str]:
        result_string_list = []
        char_ptr = 0

        while char_ptr < len(s):
            len_word = ""
            while s[char_ptr] != "#":
                len_word += s[char_ptr]
                char_ptr += 1
            char_ptr += 1
            len_word = int(len_word)
            curr_word = s[char_ptr:char_ptr+len_word]
            result_string_list.append(curr_word)
            char_ptr += len_word

        return result_string_list

