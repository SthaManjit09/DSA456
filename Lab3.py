# Part A - Recursive Functions

# Function 1: Factorial (Recursive)
def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)
print(factorial(5))

# Function 2: Linear Search (Recursive)
def linear_search(lst, key, index=0):
    if index == len(lst):
        return -1
    elif lst[index] == key:
        return index
    else:
        return linear_search(lst, key, index + 1)
print(linear_search([1, 3, 5, 7, 9], 5))  # Output: 2
    

# Function 3: Binary Search (Recursive)
def binary_search(lst, key, low=0, high=None):
	if high is None:
		high = len(lst) - 1
	if low > high:
		return -1
	mid = (low + high) // 2
	if lst[mid] == key:
		return mid
	elif lst[mid] > key:
		return binary_search(lst, key, low, mid - 1)
	else:
		return binary_search(lst, key, mid + 1, high)
print(binary_search([1, 2, 3, 4, 5, 6, 7], 4))  # Output: 3

## Function 4: Hanoi tower problem
def hanoi_tower(disks, source=1, target=3, auxiliary=2):
    if disks == 1:
        print(f"{source} to {target}")  # Base case: Move one disk directly
    else:
        # Move (disks - 1) from source to auxiliary
        hanoi_tower(disks - 1, source, auxiliary, target)
        # Move the remaining disk to the target
        print(f"{source} to {target}")
        # Move the (disks - 1) from auxiliary to target
        hanoi_tower(disks - 1, auxiliary, target, source)



### Function 1:

# Analyze the following function with respect to `number`


def function1(number):
    total = 0  # 1 (initialization)

    for i in range(0, number):  # n (loop control)
        x = (i + 1)  # n (assignment)
        total += (x * x)  # n (multiplication and addition)

    return total  # 1 (return statement)

# Let `n` represent the number passed to the `function1()` function.
# Let `T(n)` represent the number of operations needed to find the sum of squares until `number` using `function1()`.
#
# Now, `T(n)` will be:
# - 1 (initialization) + n (loop control) + n (assignment) + n (multiplication and addition) + 1 (return statement)
#
# `T(n) = 1 + n + n + n + 1`
# `T(n) = 3n + 2`
#
# The dominating term here is `n`, therefore:
# `T(n)` is **O(n)**

### Function 2:

# Analyze the following function with respect to `number`

def function2(number):
    return ((number) * (number + 1) * (2 * number + 1)) / 6  # 6 (constant arithmetic operations)

# Let `n` represent the number passed to the `function2()` function.
# Let `T(n)` represent the number of operations needed to find the sum of squares until `number` using `function2()`.
#
# Now, `T(n)` will be:
# - A constant number of arithmetic operations (multiplications, additions, and division).
#
# `T(n) = 6`
#
# There is no dominating term here, therefore:
# `T(n)` is **O(1)**

### Function 3:

# Analyze the following with respect to the length of the list.
# Note that the function call `len()` which returns the length of the list is constant (`O(1)`) with respect to the length of the list.


def function3(lst):
    for i in range(0, len(lst) - 1):  # n - 1 iterations
        for j in range(0, len(lst) - 1 - i):  # (n - 1 - i) iterations
            if lst[j] > lst[j + 1]:  # 1 comparison
                tmp = lst[j]  # 1 assignment
                lst[j] = lst[j + 1]  # 1 assignment
                lst[j + 1] = tmp  # 1 assignment

# Let `n` represent the length of the list passed to `function3()`.
# Let `T(n)` represent the number of operations needed to sort the list using `function3()`.
#
# The total number of times the inner loop will run is:
# `(n - 1) + (n - 2) + (n - 3) + ... + 1` = \( \frac{(n-1) \cdot n}{2} \)
#
# Now, `T(n)` will be:
#
# `T(n) = \frac{(n - 1) \cdot n}{2} + 3 \cdot \frac{(n - 1) \cdot n}{2}`
#
# `T(n) = 4 \cdot \frac{(n - 1) \cdot n}{2}`
#
# `T(n) = 2(n^2 - n)`
#
# The dominating term here is \( n^2 \), therefore:
# `T(n)` is **O(n^2)**

### Function 4: Hanoi Tower Problem

# The purpose is to move all the disks from tower 1 to tower 3 using tower 2.
# The rules are:
# 1. Only one disk can be moved at a time.
# 2. A disk can only be moved if it is the uppermost disk in the pole.
# 3. A larger disk can't be placed on a smaller disk.

def hanoi_tower(disks, source=1, target=3, auxiliary=2):
    if disks == 1:
        print(f"{source} to {target}")  # Base case: Move one disk directly
    else:
        # Move (disks - 1) from source to auxiliary
        hanoi_tower(disks - 1, source, auxiliary, target)
        # Move the remaining disk to the target
        print(f"{source} to {target}")
        # Move the (disks - 1) from auxiliary to target
        hanoi_tower(disks - 1, auxiliary, target, source)

# Example call:
# hanoi_tower(3)
# Output example for 3 disks:
# 1 to 3
# 1 to 2
# 3 to 2
# 1 to 3
# 2 to 1
# 2 to 3
# 1 to 3

# Time Complexity Analysis:
# Let `n` represent the number of disks.
# The recurrence relation for the time complexity is:
# T(n) = 2T(n-1) + O(1)
# Solving this recurrence gives T(n) = O(2^n).

