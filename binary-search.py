# Node class
class Node:

    # Nodes will hold their value as well as whoever's left and right
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


# Inserts a node for a given value and root node
def insert(root, value):

    # If the root node doesn't exist, set this new node as root
    if root is None:
        root = Node(value, None, None)

    # If the given value is less than the root's value,
    # place it on the left branch of the tree by calling
    # this method again recursively
    elif value < root.value:
        root.left = insert(root.left, value)

    # If the given value is greater than the root's value,
    # place it on the right branch of the tree by calling
    # this method again recursively
    else:
        root.right = insert(root.right, value)

    return root


# Traverses the tree from the given root node
def traverse(root):

    # If the node passed in doesn't exist, you're done
    if root is None:
        return

    # Use this method on the left thingy
    traverse(root.left)
    traverse(root.right)
