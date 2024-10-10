# Basic implementation of the Union Find data structure
# Assume we have n nodes labeled from 0 to n - 1

class UnionFind:
    def __init__(self, n):
        # every node is originally its own parent
        self.par = [i for i in range(n)]    
        # self.par = list(range(n)) -- also valid

        # every node originally is in its own 
        # component of size 1 - this changes during
        # the union operation
        self.rank = [1] * n

    def find(self, n) -> int:
        '''
        Finds the parent node of n 
        '''

        # can be optimized with path compression
        while n != self.par[n]:
            n = self.par[n]
        return n
    

    def union(self, n1, n2) -> bool:
        '''
        Connects two nodes together if not 
        already connected
        '''

        # find the parent of node 1 and 2
        p1 = self.find(n1)      
        p2 = self.find(n2)

        # nodes are already connected
        # cannot union together
        if p1 == p2:            
            return False
        
        # for efficiency, make bigger component
        # parent of smaller component - reduces
        # number of steps we have to take in find()

        if self.rank[p1] >= self.rank[p2]:
            # p2 is smaller, so when union it has a
            # new parent, p1
            self.par[p2] = p1

            # p1 gets all the nodes of p2, increasing
            # its rank, or size
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]

        return True
    
    def nodes_connected(self, n1, n2) -> bool:
        '''
        Returns if two nodes are connected
        '''

        # connected if parent is the same
        return self.find(n1) == self.find(n2)
    


def verify():
    n = 7
    u = UnionFind(n)

    # False, nodes not connected
    print(u.nodes_connected(0, 1))

    # True, just connected 0 and 1
    u.union(0, 1)
    print(u.nodes_connected(0, 1))

    # Rank is 2, includes 0 and 1
    print(u.rank[0])

    u.union(4, 5)
    u.union(1, 4)

    # True, 0 - 1 and 4 - 5 are connected
    # 1 to 4 connects both components
    print(u.nodes_connected(0, 5))