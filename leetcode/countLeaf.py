from sys import stdin
class Node:
    def _init_(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
class Tree:
    def _init_(self):
        self.root= None
    def insert(self,root,val):
        if self.root is None:
            self.root=Node(val)
        else:
            if root is None:
                root=Node(val)