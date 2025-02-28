import HW2
import time
import matplotlib.pyplot as plt
import numpy as np
import random

'''
Use this file to analyze the time complexity of the functions in HW1.py
You can use matplotlib and numpy to help you plot the data
Resource: https://www.w3schools.com/python/matplotlib_plotting.asp
'''
def mergeSort_TimeComplexity(A, p, r, trials):
    # Time complexity set up calling the function
    # Copy paste from project 1 structure with changing function.
    start_time = time.time()
    for _ in range(trials):
        HW2.merge_sort(A, p, r)
    end_time = time.time()
    elapsed_time = end_time - start_time
    average_runtime = elapsed_time / trials
    return average_runtime

def insertionSort_TimeComplexity(A, trials):
    start_time = time.time()
    for _ in range(trials):
        HW2.insertion_sort(A)
    end_time = time.time()
    elapsed_time = end_time - start_time
    average_runtime = elapsed_time / trials
    return average_runtime

def main():

    trials = 10 
    # Successful testing array size reaches near 1s
    array_size = 38000  
    # Increment values to graph time changes of the data size
    array_sizes = [6000, 14000, 22000, 30000, 38000]
    # Loop through each array size and find it runtime
    max_attempts = 5

    # List to stored runtime
    insertTime = []
    insertSortedTime = []

    for i in range(max_attempts):
        # First array is unsorted list
        array = [random.randint(0, 100) for _ in range(array_sizes[i])]
        # Sorted Array from 0 to array sizes
        sortedArray = [i for i in range(array_sizes[i])]
        
        # Average time return for array size and insertion sorted element function
        inserttime = insertionSort_TimeComplexity(array.copy(), trials)
        inserttimeSorted = insertionSort_TimeComplexity(sortedArray, trials)

        # Stored times for y-axis
        insertTime.append(inserttime)
        insertSortedTime.append(inserttimeSorted) 


    print(f"Insertion Sort (Array size: {array_size}, Trials: {trials}): {inserttime:.5f} seconds")

    # Successful runtime for Merge Sort to reach near 1s
    array_size = 400000
    array_sizesMerge = [0, 100000, 200000, 300000, 400000]
    sortarray_sizesMerge = [0, 200000, 400000, 600000, 800000]

    # List to stores runtime for unsorted and sorted list
    arrayMergeTime = []
    arraySortedMergeTime = []

    for j in range(max_attempts):
        # Create unsorted array int
        array = [random.randint(0, 100) for _ in range(array_sizesMerge[j])]
        # Create sorted array int
        sortedMergeArray = [i for i in range(sortarray_sizesMerge[j])]

        # Run run-time measurement return averagetime aiming for near 1s
        mergetime = mergeSort_TimeComplexity(array, 0, len(array)-1, trials)
        sortedMergeTime = mergeSort_TimeComplexity(sortedMergeArray, 0, len(array)-1, trials)
        
        # Stores the time of each j looping
        arrayMergeTime.append(mergetime)
        arraySortedMergeTime.append(sortedMergeTime)

    print(f"Merge Sort (Array size: {array_size}, Trials: {trials}): {mergetime:.5f} seconds")


    # Plotting Merge Sort
    plt.figure(figsize=(10, 5))
    plt.plot(array_sizesMerge, arrayMergeTime, label='Merge UnSorted', color='blue')
    plt.xlabel('Input Array Size (n)')
    plt.ylabel('Time (s)')
    plt.title('Merge Unsorted List Time Complexity')
    plt.grid(True)
    plt.legend()

    plt.figure(figsize=(10, 5))
    plt.plot(sortarray_sizesMerge, arraySortedMergeTime, label='Merge Sort List', color='red')
    plt.xlabel('Input Array Size (n)')
    plt.ylabel('Time (s)')
    plt.title('Merge Sorted List Time Complexity')
    plt.grid(True)
    plt.legend()

    # Plotting Insertion Sort
    plt.figure(figsize=(10, 5))
    plt.plot(array_sizes, insertTime, label='Insertion Unsorted List', color='orange')
    plt.xlabel('Input Array Size')
    plt.ylabel('Time (s)')
    plt.title('Insertion Unsorted List Time Complexity')
    plt.grid(True)
    plt.legend()

    plt.figure(figsize=(10, 5))
    plt.plot(array_sizes, insertSortedTime, label='Insertion Sorted List', color='blue')  # Use insertSortedTime here
    plt.xlabel('Input Array Size')
    plt.ylabel('Time (s)')
    plt.title('Insertion Sorted List Time Complexity')
    plt.grid(True)
    plt.legend()

    plt.show()

if __name__ == "__main__":
    main()