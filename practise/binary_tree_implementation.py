class Treenode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

node0 = Treenode(3)
node1 = Treenode(4)
node2 = Treenode(5)

node0
print(node0.key)

node0.left = node1
node0.right = node2


tree = node0
print(tree.key)



# Tree Tuple
tree_tuple = ((1,3,None), 2, (None,3,4), 5, (6,7,8))

def parse_tuple(data):
    if data is None:
        return None
    if isinstance(data, tuple) and len (data) == 3:
        node = Treenode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        return None
    else:
        node = Treenode(data)
    return node