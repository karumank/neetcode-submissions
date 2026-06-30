class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures)
        indx_stack = [0]
        ptr = 1

        while ptr < len(temperatures):
            if temperatures[ptr] > temperatures[ptr - 1]:
                while indx_stack and temperatures[ptr] > temperatures[indx_stack[-1]]:
                    idx = indx_stack.pop()
                    result[idx] = ptr - idx
                indx_stack.append(ptr)
            else: 
                indx_stack.append(ptr)
            ptr += 1
        
        return result
                

