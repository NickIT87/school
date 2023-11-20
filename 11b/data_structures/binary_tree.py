class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)


def preorder_traversal(root):
    if root:
        print(root.val, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)


def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val, end=" ")


if __name__ == "__main__":
    root = None
    keys = [50, 30, 20, 40, 70, 60, 80]

    for key in keys:
        root = insert(root, key)

    print("Inorder Traversal:")
    inorder_traversal(root)

    print("\nPreorder Traversal:")
    preorder_traversal(root)

    print("\nPostorder Traversal:")
    postorder_traversal(root)

    print("")
