class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, x):
        # Find the parent
        # While looping parent, fix any unordered child
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        
        return x

    
    def union(self, x1, x2):
        # Find parent of x1 and x2
        par1, par2 = self.find(x1), self.find(x2)
        # if same, return False
        if par1 == par2:
            return True
        # Join parents if not -> by looking at rank. put smaller rank parent under bigger rank parent
        if self.rank[par1] > self.rank[par2]:
            self.par[par2] = par1
            self.rank[par1] += self.rank[par2]
        else:
            self.par[par1] = par2
            self.rank[par2] += self.rank[par1]
        return True
        

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAcc = {}

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAcc:
                    uf.union(i, emailToAcc[e])
                else:
                    emailToAcc[e] = i
        
        emailGroup = defaultdict(list)

        for e, i in emailToAcc.items():
            leader = uf.find(i)
            emailGroup[leader].append(e)
        res = []
        for i, emails in emailGroup.items():
            res.append([accounts[i][0]] + sorted(emails))
        
        return res



        