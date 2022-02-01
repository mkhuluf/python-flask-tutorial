import json

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def toList(self):
        nodeList = []
        node = self.head
        if node is None:
            return nodeList
        while node:
            nodeList.append(node.data)
            node = node.next
        return nodeList

    def toString(self):
        linkedListStr = ""
        node = self.head
        if node is None:
            print(None)
        while node:
            linkedListStr += f"{str(node.data)} -> "
            node = node.next

        linkedListStr += " None"
        print(linkedListStr)

    def insert_at_head(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.tail = self.head

        new_node = Node(data, self.head)
        self.head = new_node

    def insert_at_tail(self, data):
        if self.head is None:
            self.insert_at_head(data)
            return

        self.tail.next = Node(data, None)
        self.tail = self.tail.next

    def getUserById(self, user_id):
        node = self.head
        while node:
            if node.data["id"] is int(user_id):
                return node.data
            node = node.next
        return None


