class Solution:
    def isValid(self, s: str) -> bool:
        
        close_braces = {")": "(", "}": "{", "]": "["}

        brace_stack = []

        for brace in s:
            if brace in close_braces:
                if len(brace_stack) <= 0:
                    return False
                curr_brace = brace_stack.pop()
                if curr_brace != close_braces[brace]:
                    return False
            else:
                brace_stack.append(brace)
        return len(brace_stack) == 0

