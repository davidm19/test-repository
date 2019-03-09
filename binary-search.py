class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def insert(root, value):
    if root is None:
        root = Node(value, None, None)
    elif value < root.value:
        root.right = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root

def traverse(root):
    if root is None:
        return

    traverse(root.left)
    traverse(root.right)
