class Node: 
    def __init__(self, data): 
        self.data = data  # 
        self.next = None  
class LinkedList: 
    def __init__(self): 
        self.head = None
    def push1(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
    def search(self, x): 
        current = self.head 
        while current != None: 
            if current.data == x: 
                return current 
            current = current.next
        return None
    def insertAfter(self, prev_node, new_data): 
        if prev_node is None: 
            return
        new_node = Node(new_data) 
        new_node.next = prev_node.next
        prev_node.next = new_node 
    def append(self, new_data): 
        new_node = Node(new_data) 
        if self.head is None: 
            self.head = new_node 
            return
        last = self.head 
        while (last.next): 
            last = last.next
        last.next =  new_node 
    def printList(self): 
        temp = self.head 
        while (temp): 
            print (temp.data) 
            temp = temp.next
    def deleteNode(self, key): 
        temp = self.head 
        if (temp is not None): 
            if (temp.data == key): 
                self.head = temp.next
                temp = None
                return
        while(temp is not None): 
            if temp.data == key: 
                break
            prev = temp 
            temp = temp.next
        if(temp == None): 
            return
        prev.next = temp.next
        temp = None
def deleteKey(head_ref, key):
        temp = head_ref
        prev = None
        while (temp != None and temp.data == key):
            head_ref = temp.next 
            temp = head_ref       
        while (temp != None):
            while (temp != None and temp.data != key):
                prev = temp
                temp = temp.next
            if (temp == None):
                return head_ref
            prev.next = temp.next
            temp = prev.next
        return head_ref
def removeFirstNode(head): 
        if not head: 
            return None
        temp = head 
        head = head.next
        temp = None
        return head
ans =LinkedList() 
while True:
    l = [int(i) for i in input().split()]
    if l[0] == 0:
        ans.push1(l[1])
    elif l[0] == 1:
        ans.append(l[1])
    elif l[0] == 2:
        index=ans.search(l[1])
        if index != None:
            index.insertAfter(index,l[2])
    elif l[0] == 3:
        ans.deleteNode(l[1])
    elif l[0] == 4:
        ans=deleteKey(ans.head,l[1])
    elif l[0] == 5:
            removeFirstNode(ans.head)
    else:
        break
ans.printList()