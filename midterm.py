# Question No 1
def second_highest(lst):
    unique_values = sorted(set(lst), reverse=True)  # Remove duplicates and sort in descending order
    return unique_values[1] if len(unique_values) > 1 else None

# Test cases
print(second_highest([4, 1, 2, 2, 3, 4, 5]))  # Output: 4

# Question No 2
def hofstadter_q(n):
    if n < 1:
        return None  
    
    q_seq = [None, 1, 1]  # Start with Q(1) = 1, Q(2) = 1
    
    for i in range(3, n + 1):
        q_seq.append(q_seq[i - q_seq[i - 1]] + q_seq[i - q_seq[i - 2]])
    
    return q_seq[n]


q_values = [hofstadter_q(i) for i in range(1, 11)]
print(q_values)

# Question NO 3
# Analysis 
# Q1: Finding the Second Highest Unique Value
def second_highest(lst):
    # Convert list to a set to remove duplicates (O(n))
    unique_values = sorted(set(lst), reverse=True)  # Sort unique values in descending order (O(n log n))
    return unique_values[1] if len(unique_values) > 1 else None  # Access second element (O(1))

# Time Complexity:
# - Removing duplicates: O(n)
# - Sorting: O(n log n)
# - Accessing the second element: O(1)
# Overall Complexity: O(n log n)
# Space Complexity: O(n) (for storing unique values)

# ---------------------------------------------------------------------

# Q2: Generating the nth Hofstadter Q-sequence number
def hofstadter_q(n):
    if n < 1:
        return None
    
    q_seq = [None, 1, 1]  # Initial values, O(1)
    
    for i in range(3, n + 1):  # Loop runs O(n) times
        q_seq.append(q_seq[i - q_seq[i - 1]] + q_seq[i - q_seq[i - 2]])  # Each operation O(1)

    return q_seq[n]

# Time Complexity:
# - Initializing list: O(1)
# - Iterating from 3 to n: O(n)
# - Each lookup and append: O(1) per iteration, total O(n)
# Overall Complexity: O(n)
# Space Complexity: O(n) (for storing the sequence)

# ---------------------------------------------------------------------

# Comparison:
# - Hofstadter Q-sequence (Q2): O(n)
# - Merge Sort: O(n log n) (slower than Q2)
# - Binary Search: O(log n) (faster than Q2)

# Conclusion:
# - Q2 is **faster** than Merge Sort.
# - Q2 is **slower** than Binary Search.

# Question No 4
import math

def print_primes(n):
    if n < 2:
        print("No prime numbers.")
        return

    for i in range(2, n + 1):  # O(n) loop
        is_prime = True
        for divisor in range(2, int(math.sqrt(i)) + 1):  # O(sqrt(n)) loop
            if i % divisor == 0:
                is_prime = False
                break
        if is_prime:
            print(i)

# Time Complexity:
# - Outer loop runs O(n) times
# - Inner loop runs O(sqrt(n)) times in worst case
# - Overall: O(n * sqrt(n)) = O(n^1.5)
# - Space Complexity: O(1) (only a few variables stored)

# Performance Ranking (Slowest to Fastest):
# 1. Bubble Sort: O(n^2) (slowest)
# 2. Finding all primes up to n: O(n^1.5)
# 3. Merge Sort: O(n log n) (fastest)

# Question No 5
# Q5: Time Complexity Analysis of T(n) = 2n + T(n/5)

# Expanding the recurrence:
# T(n) = 2n + 2(n/5) + 2(n/25) + ... + 2(n/5^k)
# This forms a geometric series.

# Stopping Condition:
# We stop when n/5^k ≈ 1, so k = log_5(n).

# Sum of the Series:
# The sum of this geometric series simplifies to O(n).

# Final Complexity:
# T(n) = O(n)

# Comparison with Other Algorithms:
# - Binary Search: O(log n) → Faster than our function.
# - Merge Sort: O(n log n) → Slower than our function.

# Conclusion:
# - T(n) = O(n) is **slower** than Binary Search (O(log n)).
# - T(n) = O(n) is **faster** than Merge Sort (O(n log n)).

# Question NO 6
# Q6: Memory Usage - Arrays vs. Linked Lists

# **Arrays (Contiguous Memory Allocation)**
# - ✅ Memory-efficient: Uses contiguous memory blocks, reducing overhead.
# - ✅ Fast index-based access (O(1)) due to direct memory addressing.
# - ❌ Fixed size: Requires resizing (copying to a new larger array) when full.
# - ❌ Wastes memory if allocated size is larger than needed.

# **Linked Lists (Dynamic Memory Allocation)**
# - ✅ Dynamic size: No need to preallocate memory, grows as needed.
# - ✅ No memory wastage due to resizing like arrays.
# - ❌ Extra memory overhead: Each node stores additional pointers (next/prev).
# - ❌ Slower access (O(n)) since elements are scattered in memory.

# **Conclusion:**
# - **Use arrays** when memory is limited and fast access is required.
# - **Use linked lists** when dynamic resizing is needed, despite higher overhead.

# Question NO 7
class sorted_LList:
    class Node:
        def __init__(self, data, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

    def __init__(self):
        self.front = None  # Smallest element
        self.back = None   # Largest element

    # **Insert function to keep the list sorted**
    def insert(self, val):
        new_node = self.Node(val)
        
        # Case 1: List is empty
        if self.front is None:
            self.front = self.back = new_node
            return
        
        # Case 2: Insert at the front (new smallest element)
        if val < self.front.data:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
            return
        
        # Case 3: Insert at the back (new largest element)
        if val > self.back.data:
            new_node.prev = self.back
            self.back.next = new_node
            self.back = new_node
            return
        
        # Case 4: Insert in the middle (find correct position)
        curr = self.front
        while curr and curr.data < val:
            curr = curr.next
        
        prev_node = curr.prev
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = curr
        curr.prev = new_node

    # **Function to find the smallest element**
    def min(self):
        return self.front.data if self.front else None  # O(1) operation

    # **Function to find the largest element**
    def max(self):
        return self.back.data if self.back else None  # O(1) operation

    # **Optimized Search using Sorted & Doubly Linked List Properties**
    def search(self, key):
        # Start searching from both ends (front & back)
        left = self.front
        right = self.back
        
        while left and right and left != right and right.next != left:
            if left.data == key:
                return left  # Key found at the left side
            if right.data == key:
                return right  # Key found at the right side
            
            left = left.next   # Move left pointer forward
            right = right.prev  # Move right pointer backward
        
        return None  # Key not found

# **Usage Example**
ll = sorted_LList()
ll.insert(10)
ll.insert(5)
ll.insert(20)
ll.insert(15)

print("Min:", ll.min())  # Output: 5
print("Max:", ll.max())  # Output: 20
print("Search 15:", "Found" if ll.search(15) else "Not Found")  # Output: Found
print("Search 25:", "Found" if ll.search(25) else "Not Found")  # Output: Not Found
# Q7: Sorted Doubly Linked List Implementation

# **Insert (O(n))**:
# - Finds correct position & inserts node while keeping list sorted.

# **Min/Max (O(1))**:
# - Direct access to smallest (front) & largest (back) elements.

# **Optimized Search (O(n))**:
# - Uses two-pointer approach (from front & back) to improve efficiency.
