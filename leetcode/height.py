from collections import deque
from sys import stdin 
class Node:
    def __init__(self,value=None,bool=True):
        self.val=value 
        self.left=None
        self.right=None
    def set_val(self,val):
        self.val=val
def insert(tree,node):
    if tree is None:
        return 
    if tree.val==node.val:
        return 
    if tree.val<node.val:
        if tree.right is not None:
            insert(tree.right,node)
        else:
            tree.right=node
            return 
    else:
        if tree.left is not None:
            insert(tree.left,node)
        else:
            tree.left=node
            return
def height(tree):
        if tree is None:
            return 0
        left = height(tree.left)
        right = height(tree.right)
        if left > right:
            return left + 1
        else:
            return right + 1
def createTree(list):
        root=Node(None)
        for node in list:
            if root.val is None:
                root.set_val(node)
            else:
                new_node=Node(node)
                insert(root,new_node)
        return root
get = stdin.readline()
list = deque()
while get != '3\n':
    get = [int(s) for s in get.split()]
    if get[0] == 0:
        list.appendleft(get[1])
    else:
        if get[0] == 1:
            list.append(get[1])
        else:
            if get[1] in list:
                i = list.index(get[1])
                if i == len(list) - 1:
                    list.append(get[2])
                else:
                    list.insert(i + 1, get[2])
    get = stdin.readline()
root=createTree(list)
height=height(root)
print(height)