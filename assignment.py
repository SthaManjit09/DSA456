import random
import time
import matplotlib.pyplot as plt

def bubble_sort(my_list):
    steps = 0
    n = len(my_list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            steps += 1  # Comparison
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                steps += 3  # Swap operations
    return steps

def selection_sort(my_list):
    steps = 0
    n = len(my_list)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            steps += 1  # Comparison
            if my_list[j] < my_list[min_idx]:
                min_idx = j
        if min_idx != i:
            my_list[min_idx], my_list[i] = my_list[i], my_list[min_idx]
            steps += 3  # Swap operations
    return steps

def insertion_sort(my_list):
    steps = 0
    for i in range(1, len(my_list)):
        curr = my_list[i]
        j = i
        steps += 1  # Assignment
        while j > 0 and my_list[j - 1] > curr:
            my_list[j] = my_list[j - 1]
            j -= 1
            steps += 2  # Comparison and assignment
        my_list[j] = curr
        steps += 1  # Final placement
    return steps

def quick_sort(my_list, left=0, right=None):
    if right is None:
        right = len(my_list) - 1
    steps = 0
    
    while left < right:
        pivot_index, new_steps = partition(my_list, left, right)
        steps += new_steps
        
        if pivot_index - left < right - pivot_index:
            steps += quick_sort(my_list, left, pivot_index - 1)
            left = pivot_index + 1
        else:
            steps += quick_sort(my_list, pivot_index + 1, right)
            right = pivot_index - 1
    
    return steps

def partition(my_list, left, right):
    steps = 0
    pivot = my_list[right]
    i = left - 1
    for j in range(left, right):
        steps += 1  # Comparison
        if my_list[j] < pivot:
            i += 1
            my_list[i], my_list[j] = my_list[j], my_list[i]
            steps += 3  # Swap operations
    my_list[i + 1], my_list[right] = my_list[right], my_list[i + 1]
    steps += 3  # Final pivot swap
    return i + 1, steps

def generate_random_list(size):
    return [random.randint(1, size) for _ in range(size)]

def measure_execution_time():
    sizes = [10, 50, 100, 200, 500]  # Reduced max size to 500
    sorting_algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Quick Sort": quick_sort
    }
    execution_times = {alg: [] for alg in sorting_algorithms}
    timeout = 5  # Set a timeout of 5 seconds per sorting function
    
    for n in sizes:
        test_list = list(range(n, 0, -1))  # Worst case scenario
        for alg_name, sort_function in sorting_algorithms.items():
            start_time = time.time()
            sort_function(test_list.copy())
            end_time = time.time()
            execution_time = end_time - start_time
            
            if execution_time > timeout:
                print(f"Skipping {alg_name} for n={n}, took too long (> {timeout} sec).")
                execution_times[alg_name].append(None)  # Mark as skipped
                continue
            
            execution_times[alg_name].append(execution_time)
    
    for alg_name, times in execution_times.items():
        plt.plot(sizes, times, label=alg_name)
    
    plt.xlabel("n (List Size)")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Sorting Algorithm Execution Time")
    plt.legend()
    plt.show()

# Run execution time measurement
measure_execution_time()
