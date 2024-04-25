class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def printLeafNodes(node):
    if node is not None:
        if node.left is None and node.right is None:
            print(node.data, end=' ')
        else:
            if node.left:
                printLeafNodes(node.left)
            if node.right:
                printLeafNodes(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)

# დაბეჭვდა ყვავილების
print("ხის ყვავილებია: ", end='')
printLeafNodes(root)
