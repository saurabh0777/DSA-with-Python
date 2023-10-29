'''
Creating a binary search tree in Python involves defining a class for the nodes of the tree and
implementing methods to insert elements into the tree while maintaining the binary search tree properties.
Here's an example implementation:

In this example, the Node class represents each node in the binary search tree,
with left and right attributes pointing to the left and right children, respectively.
The insert function inserts a new key into the BST while maintaining the binary search tree property.
The inorder_traversal function performs an inorder traversal of the BST, printing the nodes in sorted order.

You can modify the insert function to handle duplicates or implement other operations like search
or deletion based on your requirements.


'''


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    # If the tree is empty, create a new node
    if root is None:
        return Node(key)

    # Otherwise, recur down the tree
    if key < root.val:
        root.left = insert(root.left, key)
    elif key > root.val:
        root.right = insert(root.right, key)

    # Return the (unchanged) node pointer
    return root


# Function to do inorder traversal of the tree
def inorder_traversal(root):
    if root:
        # Traverse the left subtree
        inorder_traversal(root.left)
        # Visit the root node
        print(root.val)
        # Traverse the right subtree
        inorder_traversal(root.right)


# Example usage
if __name__ == "__main__":
    r = Node(50)
    r = insert(r, 30)
    r = insert(r, 20)
    r = insert(r, 40)
    r = insert(r, 70)
    r = insert(r, 60)
    r = insert(r, 80)

    # Print inorder traversal of the BST
    inorder_traversal(r)
