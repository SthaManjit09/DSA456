class BST:
    class Node:
        def __init__(self, data=None, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BST.Node(data)
        else:
            curr = self.root
            inserted = False
            while not inserted:
                if data < curr.data:
                    if curr.left is not None:
                        curr = curr.left
                    else:
                        curr.left = BST.Node(data)
                        inserted = True
                else:
                    if curr.right is not None:
                        curr = curr.right
                    else:
                        curr.right = BST.Node(data)
                        inserted = True

    def search(self, data):
        curr = self.root
        while curr is not None:
            if data < curr.data:
                curr = curr.left
            elif data > curr.data:
                curr = curr.right
            else:
                return curr
        return None

    # Function 1: Convert BST to sorted list
    def BST_to_list(self):
        def in_order(node):
            if node is None:
                return []
            return in_order(node.left) + [node.data] + in_order(node.right)
        return in_order(self.root)

    # Function 2: Get the height of the BST
    def height(self):
        def _height(node):
            if node is None:
                return -1
            left_height = _height(node.left)
            right_height = _height(node.right)
            return 1 + max(left_height, right_height)
        return _height(self.root)

    # Function 3: Get the maximum value in the BST
    def max(self):
        curr = self.root
        while curr.right is not None:
            curr = curr.right
        return curr.data

    # Function 4: Get the minimum value in the BST
    def min(self):
        curr = self.root
        while curr.left is not None:
            curr = curr.left
        return curr.data


my_bst = BST()
my_bst.insert(5)
my_bst.insert(6)
my_bst.insert(4)
my_bst.insert(7)
my_bst.insert(3)
my_bst.insert(8)

# Convert BST to sorted list
print(my_bst.BST_to_list())  # Output: [3, 4, 5, 6, 7, 8]

# Get the height of the BST
print(my_bst.height())  # Output: 2

# Get the maximum value in the BST
print(my_bst.max())  # Output: 8

# Get the minimum value in the BST
print(my_bst.min())  # Output: 3
