class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

# Example usage:
# Creating a tree
if __name__ == '__main__':
    root = TreeNode("Root")

    child1 = TreeNode("Child 1")
    child2 = TreeNode("Child 2")

    root.add_child(child1)
    root.add_child(child2)

    grandchild1 = TreeNode("Grandchild 1")
    grandchild2 = TreeNode("Grandchild 2")

    child1.add_child(grandchild1)
    child1.add_child(grandchild2)

    # Traversing the tree
    def traverse_tree(node):
        print(node.data)
        for child in node.children:
            traverse_tree(child)

    traverse_tree(root)
