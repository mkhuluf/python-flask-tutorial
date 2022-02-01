class Node: 
    def __init__(self, data, next):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def peek(self):
        return self.top
    
    def push(self, data):
        nextNode = self.top
        new_top = Node(data, nextNode)
        self.top = new_top

    def pop(self):
        if self.top is None:
            return None
        
        removed = self.top
        self.top = self.top.next
        return removed