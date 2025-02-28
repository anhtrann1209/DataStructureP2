import HW3
import time
import matplotlib.pyplot as plt
import numpy as np

'''
Use this file to analyze the time complexity of the functions in HW3.py
You can use matplotlib and numpy to help you plot the data
Resource: https://www.w3schools.com/python/matplotlib_plotting.asp
'''
import time
import random

def bruteForceQuickHull_TimeComplexity(points, trials):
    start_time = time.time()
    for _ in range(trials):
        HW3.convex_hull(points)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time / trials

def quickHull_TimeComplexity(points, trials):
    start_time = time.time()
    for _ in range(trials):
        HW3.quick_hull_start(points)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time / trials


def main():
    trials = 10
    point_sizes_bf = [200, 250, 300, 350, 400]  # Brute Force sizes
    point_sizes_qh = [100000, 200000, 3000000, 4000000, 5000000]  # QuickHull sizes

    brute_force_times = []
    quick_hull_times = []
    
    # Measuring Brute Force QuickHull Time Complexity
    for size in point_sizes_bf:
        points = HW3.generate_points(size)
        bf_time = bruteForceQuickHull_TimeComplexity(points, trials)
        brute_force_times.append(bf_time)
        print(f"Brute Force QuickHull (Size: {size}, Trials: {trials}): {bf_time:.5f} sec")

    # Measuring QuickHull Time Complexity
    for size_qh in point_sizes_qh:
        points2 = HW3.generate_points(size_qh)
        qh_time = quickHull_TimeComplexity(points2, trials)
        quick_hull_times.append(qh_time)
        print(f"QuickHull (Size: {size_qh}, Trials: {trials}): {qh_time:.5f} sec")

    # Plotting Results
    plt.figure(figsize=(10,5))
    plt.plot(point_sizes_bf,brute_force_times)
    plt.xlabel("Input sizes (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Runtime Analysis of Brute Force Quick Hull")
    plt.grid(True)
    plt.legend()
    # plt.show()

    plt.figure(figsize=(10,5))
    plt.plot(point_sizes_qh, quick_hull_times)
    plt.xlabel("Input sizes (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Runtime Analysis of Quick Hull")
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()