class UnionFind:
    def __init__(self, size):
        self.size = size  # number of elements in union find

        # each component is originally of size 1
        self.sz = [1] * size  # track the size of each component

        # link to itself (self root)
        self.id = [
            i for i in range(size)
        ]  # id[i] points to the parent of i, if id[i] = i then i is a root node
        self.num_components = size  # number of components in union find

    # Find which component/set 'p' belongs to, takes amortized constant time.
    def find(self, p):
        # find the root of the component/set
        root = p
        while root != self.id[root]:
            root = self.id[root]

        # compress the path leading back to the root.
        # doing this operation is called "path compression"
        # and is what gives us amortized time complexity.
        while p != root:
            next = self.id[p]
            self.id[p] = root
            p = next

        return root

    # unify the components/sets containing elements 'p' and 'q'
    def unify(self, p, q):
        root1 = self.find(p)
        root2 = self.find(q)

        # these elements are already in the same group!
        if root1 == root2:
            return

        # merge two components/sets together
        # merge smaller component/set into the larger one
        if self.sz[root1] < self.sz[root2]:
            self.sz[root2] += self.sz[root1]
            self.id[root1] = root2
        else:
            self.sz[root1] += self.sz[root2]
            self.id[root2] = root1

        # since the roots found are different we know that the
        # number of components/sets has decreased by one
        self.num_components -= 1

    # return whether or not the elements 'p' and
    # 'q' are in the same components/set.
    def connected(self, p, q):
        return self.find(p) == self.find(q)

    # return the size of the components/set 'p' belongs to
    def component_size(self, p):
        return self.sz[self.find(p)]

    # return the number of elements in this UnionFind/Disjoint set
    def size(self):
        return self.size

    # returns the number of remaining components/sets
    def components(self):
        return self.num_components
