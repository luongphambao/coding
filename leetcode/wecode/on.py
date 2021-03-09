# class newNode:  
  
#     # Constructor to create a new node  
#     def __init__(self, data):  
#         self.data = data  
#         self.left = None
#         self.right = None
# def iterativeSearch(root, key): 
#     while root != None: 
#         if key > root.data:  
#             root = root.right 
#         elif key < root.data: 
#             root = root.left  
#         else: 
#             return 1 # if the key is found return 1  
#     return 0
# def insert(Node, data): 
#     if Node == None: 
#         return newNode(data)  
#     if data < Node.data:  
#         Node.left = insert(Node.left, data)  
#     elif data > Node.data:  
#         Node.right = insert(Node.right, data)
#     return Node 
# ans=None
# while True:
#     l = [int(i) for i in input().split()]
#     if l[0] == 1:
#         ans=insert(ans,l[1])
#     elif l[0] == 2:
#         print(iterativeSearch(ans,l[1]))
#     else:
#         break

ans=set()
while True:
    l = [int(i) for i in input().split()]
    if l[0] == 1:
        ans.add(l[1])
    elif l[0] == 2:
        print(int(l[1] in ans))
    elif l[0]==3:
        if l[1] in ans:
            ans.remove(l[1])
    else:
        break