class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        incoming = {i:0 for i in range(1, n + 1) }
        outgoing = {i:0 for i in range(1, n + 1) }

        for src, dst in trust:
            incoming[dst] += 1
            outgoing[src] += 1
        
        for i in range(1, n + 1):
            if outgoing[i] == 0 and incoming[i] == n - 1:
                return i
        
        return -1