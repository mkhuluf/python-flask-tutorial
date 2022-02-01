from sqlalchemy import false


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insertHelper(self, data, node):
        if data["id"] < node.data["id"]:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insertHelper(data, node.left)
        elif data["id"] > node.data["id"]:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insertHelper(data, node.right)
        else:
            return 


    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insertHelper(data, self.root)

    
    def searchHelper(self, blog_post_id, node):
        if blog_post_id == node.data["id"]:
            return node.data

        if blog_post_id < node.data["id"] and node.left is not None:
            if blog_post_id == node.data["id"]:
                return node.left.data
            return self.searchHelper(blog_post_id, node.left)

        if blog_post_id > node.data["id"] and node.right is not None:
            if blog_post_id == node.data["id"]:
                return node.right.data
            return self.searchHelper(blog_post_id, node.right)


    def search(self, blog_post_id):
        blog_post_id = int(blog_post_id)
        if self.root is None:
            return false

        return self.searchHelper(blog_post_id, self.root)
