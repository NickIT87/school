import graphviz

class Tree(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None
    root = Tree(preorder[0])
    root_index = inorder.index(root.val)
    root.left = build_tree(preorder[1:root_index+1], inorder[:root_index])
    root.right = build_tree(preorder[root_index+1:], inorder[root_index+1:])
    return root

def visualize_tree(node, graph):
    if node is None:
        return
    graph.node(str(node.val))  # Create a node in the graph
    if node.left is not None:
        graph.edge(str(node.val), str(node.left.val))  # Connect node to its left child
        visualize_tree(node.left, graph)
    if node.right is not None:
        graph.edge(str(node.val), str(node.right.val))  # Connect node to its right child
        visualize_tree(node.right, graph)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
root = build_tree(preorder, inorder)

graph = graphviz.Graph()
visualize_tree(root, graph)
graph.render('binary_tree', format='png', view=True)
