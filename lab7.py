from random import sample
from typing import List
import matplotlib.pyplot as plt

# --- Node Class ---
class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None

# --- Binary Search Tree Class ---
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data: int):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data: int, node: Node):
        if data < node.data:
            if node.left:
                self._insert(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self._insert(data, node.right)
            else:
                node.right = Node(data)

    def inorder(self, node: Node) -> List[int]:
        if not node:
            return []
        return self.inorder(node.left) + [node.data] + self.inorder(node.right)

    def height(self, node: Node) -> int:
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def imbalance(self, node: Node) -> int:
        if not node:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return abs(left_height - right_height)


class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1  # Required for balance calculations

class AVLTree:
    def __init__(self):
        self.root = None
        self.rotation_count = 0  # To count rotations performed

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if not node:
            return AVLNode(data)
        elif data < node.data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        balance = self._get_balance(node)

        # Left Heavy
        if balance > 1:
            if data < node.left.data:  # Left-Left
                self.rotation_count += 1
                return self._rotate_right(node)
            else:  # Left-Right
                self.rotation_count += 2
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        # Right Heavy
        if balance < -1:
            if data > node.right.data:  # Right-Right
                self.rotation_count += 1
                return self._rotate_left(node)
            else:  # Right-Left
                self.rotation_count += 2
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

    def _height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        return self._height(node.left) - self._height(node.right)

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        # Rotate
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        # Rotate
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y

    def inorder(self, node):
        if not node:
            return []
        return self.inorder(node.left) + [node.data] + self.inorder(node.right)

# --- Helper Functions ---
def generate_permutation(n: int) -> List[int]:
    return sample(range(1, n + 1), n)

def build_bst(data: List[int]) -> BinarySearchTree:
    bst = BinarySearchTree()
    for d in data:
        bst.insert(d)
    return bst

def plot_histogram(data: List[int], title: str):
    plt.hist(data, bins=range(min(data), max(data) + 2), edgecolor='black', align='left')
    plt.title(title)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(axis='y')
    plt.show()

# --- Main Execution ---
# Display sample tree for demo
data = generate_permutation(20)
print("Generated Data:", data)

bst = build_bst(data)
print("Inorder Traversal of BST:", bst.inorder(bst.root))
print("Height of BST:", bst.height(bst.root))
print("Imbalance at root:", bst.imbalance(bst.root))

# --- Height Histogram from 1000 Trees ---
heights = []
for _ in range(1000):
    data = generate_permutation(20)
    bst = build_bst(data)
    heights.append(bst.height(bst.root))

plot_histogram(heights, "Histogram of BST Heights (1000 Random Trees)")

# --- Imbalance Histogram from 1000 Trees ---
imbalances = []
for _ in range(1000):
    data = generate_permutation(20)
    bst = build_bst(data)
    imbalances.append(bst.imbalance(bst.root))


# Show + Save Figure_1.png
plt.figure()
plt.hist(heights, bins=range(min(heights), max(heights) + 2), edgecolor='black', align='left', color='skyblue')
plt.title("Histogram of BST Heights (1000 Random Trees)")
plt.xlabel("Height")
plt.ylabel("Frequency")
plt.grid(axis='y')
plt.tight_layout()
plt.savefig("C:/Users/Acer/Desktop/Figure_1.png")# Saved in working directory

# Generate Imbalance Data
imbalances = []
for _ in range(1000):
    data = generate_permutation(20)
    bst = build_bst(data)
    imbalances.append(bst.imbalance(bst.root))

# Show + Save Figure_2.png
plt.figure()
plt.hist(imbalances, bins=range(min(imbalances), max(imbalances) + 2), edgecolor='black', align='left', color='orange')
plt.title("Histogram of BST Imbalances (1000 Random Trees)")
plt.xlabel("Imbalance")
plt.ylabel("Frequency")
plt.grid(axis='y')
plt.tight_layout()
plt.savefig("C:/Users/Acer/Desktop/Figure_2.png") # Saved in working directory

# AVL Example - Worst-case Linear Tree
print("\n--- Rebalancing Example ---")
worst_case = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
unbalanced_bst = build_bst(worst_case)
print("BST Inorder:", unbalanced_bst.inorder(unbalanced_bst.root))
print("BST Height:", unbalanced_bst.height(unbalanced_bst.root))

avl = AVLTree()
for value in worst_case:
    avl.insert(value)

print("AVL Inorder:", avl.inorder(avl.root))
print("AVL Height:", avl._height(avl.root))
print("AVL Rotations:", avl.rotation_count)