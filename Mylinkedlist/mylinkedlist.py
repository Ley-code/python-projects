class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class mylinkedlist:
    def __init__(self):
        self.head = node()
    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node
    def display(self):
        lst = []
        cur_node = self.head
        while cur_node.next!=None:
            cur_node = cur_node.next 
            lst.append(cur_node.data)
        print(lst)
    def length(self):
        cur = self.head
        total = 0
        while cur.next!=None:
            total+=1
            cur = cur.next
        return total
    def get(self,index):
        if index>= self.length():
            print("ERROR Index out of range")
            return
        cur = self.head
        cur_index = 0
        while True:
            cur = cur.next
            if index == cur_index:
                return cur.data
            cur_index+=1 
    def delete(self,index):
        cur = self.head
        cur_index = 0
        while True:
            last = cur
            cur = cur.next
            if cur_index == index:
                last.next = cur.next
                return
            cur_index+=1
linkedlists = mylinkedlist()
linkedlists.append(1)
linkedlists.append(2)
linkedlists.append(3)
linkedlists.delete(0)
linkedlists.display()
print(linkedlists.get(3))
