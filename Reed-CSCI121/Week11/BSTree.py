class BSTNode:
    def __init__(self,k,v):
        self.key = k
        self.value = v
        self.left = None
        self.right = None

class BSTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return (self.root == None)

    def get_value(self, k): # tree search
        n = self.root
        while n != None:
            if n.key == k:
                return n.value
            elif n.key > k:
                n = n.left
            else:
                n = n.right
        return None

    def set_value(self, k, v): # tree insertion
        p = None
        n = self.root

        while n != None:
            p = n
            if k == n.key:
                n.value = v
                return
            elif k < n.key:
                n = n.left
            else:
                n = n.right

        e = BSTNode(k,v)
        if p == None:
            self.root = e
        elif k < p.key:
            p.left = e
        else:
            p.right = e

    def min_key(self):
        if self.root == None:
            return None
        else:
            n = self.root
            while n.left != None:
                n = n.left
            return n.key

    def size(self): # tree traversal

        def subtree_size(n):
            if n == None:
                return 0
            else:
                return 1 + subtree_size(n.left) + subtree_size(n.right)

        return subtree_size(self.root)

    def as_list(self):

        def subtree_list(n):
            if n == None:
                return []
            else:
                return subtree_list(n.left) + [(n.key,n.value)] + subtree_list(n.right)

        return subtree_list(self.root)

    def as_string(self):
        kvs = self.as_list()
        if len(kvs) == 0:
            return "{}"
        else:
            s = "{"
            for kv in kvs[:-1]:
                s += repr(kv[0])+": "+repr(kv[1])+", " 
            kv = kvs[-1]
            s += repr(kv[0])+": "+repr(kv[1])+"}"
            return s
    def search_path(self,k):
        #Like get, it should search through the tree looking for that key. 
        #It should return a list of strings describing the path taken from the root node 
        #to search for that key, a series of "L" and "R". 
        #If the key is in the tree, then the list returned describes where in the tree that key's node sits. 
        #If the key is not in the tree, then the list returned describes where in the tree that key's node would be placed were it to be inserted into the tree.
        placeholderlist = []

        n = self.root
        while n != None:
            if n.key == k:
                n = None
            elif n.key > k:
                placeholderlist.append("L")
                n = n.left
            else:
                placeholderlist.append("R")
                n = n.right
        return placeholderlist

    def apply(self, f):
        #takes a function of the values for the nodes in the search tree
        #should modify the value of each node n to instead store f(n.value)
        def makethisrecursion(n):
            if n == None:
                return
            else:
                n.value = f(n.value)
                makethisrecursion(n.left)
                makethisrecursion(n.right)
        
        makethisrecursion(self.root)

    def height(self):
        #height: longest search path to a node in a non-empty tree.
        #If tree is empty, height is -1
        if self.is_empty():
            return -1
        templongestpath = 0
        travelpath = -1

        def subtree_travelling(n, travelpath, templongestpath):
            if n == None:
                if travelpath > templongestpath:
                    templongestpath = travelpath
                    return templongestpath
                else:
                    return 0 
            else:
                travelpath0 = travelpath +1
                a = subtree_travelling(n.left, travelpath0, templongestpath)
                b = subtree_travelling(n.right, travelpath0, templongestpath)

                if a > b:
                    return a
                else:
                    return b
        return subtree_travelling(self.root, travelpath, templongestpath)

    def delete_max(self):
        #deletes the node with the largest key. The rest of the nodes should remain in the tree.

        #If x doesn't have a right branch then x is the maximum node. 
        #We "delete" it by focusing on prevx.left (the new max node). 

        if self.is_empty():
            pass
        else:
            tempspot = self.root
            prevspot = None
            while tempspot.right != None:
                prevspot = tempspot
                tempspot = tempspot.right
            if prevspot == None:#no node larger than the root
                self.root = self.root.left
            else:
                if tempspot.left!= None:
                    prevspot.right = tempspot.left
                    tempspot = None
                else:
                    prevspot.right = None
                #account for any possible lesser-value nodes attached to the largest node?


    def __repr__(self):
        return self.as_string()

    __str__ = __repr__

    def __bool__(self):
        return not self.is_empty()

    def __contains__(self,k):
        return (self.get_value(k) != None)

    def __len__(self):
        return (self.size())

    def __getitem__(self,k):
        return self.get_value(k)

    def __setitem__(self,k,v):
        return self.set_value(k,v)

