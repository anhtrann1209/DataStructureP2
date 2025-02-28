import HW1
import time
import matplotlib.pyplot as plt
import numpy as np

'''
Use this file to analyze the time complexity of the functions in HW1.py
You can use matplotlib and numpy to help you plot the data
Resource: https://www.w3schools.com/python/matplotlib_plotting.asp
'''

# Number of trials is a number you have to tweak until you
# get an elapsed time that is closer to 1 second.
# Elapsed time is the time before you average by the number
# of trials.
def power_brute_force_timeComplexity(x, n, trials):

    start_time = time.time()
    for _ in range(trials):
        HW1.power_brute_force(x, n)
    end_time = time.time()
    elapsed_time = end_time - start_time
    average_runtime = elapsed_time / trials

    return average_runtime

def power_iterative_timeComplexity(x, n, trials):

    start_time = time.time()
    for _ in range(trials):
        HW1.power_iterative(x, n)
    end_time = time.time()
    elapsed_time = end_time - start_time
    average_runtime = elapsed_time / trials

    return average_runtime

def power_recursive_timeComplexity(x, n, trials):

    start_time = time.time()
    for _ in range(trials):
        HW1.power_recursive(x, n)
    end_time = time.time()
    elapsed_time = end_time - start_time
    average_runtime = elapsed_time / trials

    return average_runtime

def polynomial_brute_force_timeComplexity(A, x, trials):

    start_time = time.time()
    for _ in range(trials):
        HW1.polynomial_brute_force(A, x)
    end_time = time.time()
    elapsed_time = end_time - start_time
    average_runtime = elapsed_time / trials
    
    return average_runtime

def polynomial_horners_timeComplexity(A, x, trials):

    start_time = time.time()
    for _ in range(trials):
        HW1.polynomial_horners(A, x)
    end_time = time.time()
    elapsed_time = end_time - start_time
    average_runtime = elapsed_time / trials

    return average_runtime

def main():
    trials = 10
    x = 1000
    n = 10000
    input_size = [60000,80000,100000]
    listPowerBrute = []
    listPowerIterative = []
    recursive_size = [100000, 300000, 500000]
    recursiveList = []
    poly_InputSizeA = [1001, 2001, 3001]
    polynomialBruteList = []
    B = list(range(1, 50001))
    poly_InputSizeB = [10001, 30001, 50001]
    polynomialHornersT = []
    
    #1
    for i in range(3):
        powerBruteTime = power_brute_force_timeComplexity(10, input_size[i], 10)
        powerIterativeTime = power_iterative_timeComplexity(10, input_size[i], 10)

        listPowerBrute.append(powerBruteTime)
        listPowerIterative.append(powerIterativeTime)

    for element in listPowerBrute:
        print(f"Average Power Brute runtime: {element}")

    # #2
    for pBrute in listPowerIterative:
        print(f"Average Power Iterative runtime: {pBrute}")

    # #3
    for j in range(3):
        powerRecursiveTime = power_recursive_timeComplexity(30000, recursive_size[j], 100)
        recursiveList.append(powerRecursiveTime)

    for t in recursiveList:
        print(f"Average Power Recursive runtime: {t}")


    #Polynomials sum
    #4
    for k in range(3):
        A = list(range(1, poly_InputSizeA[k]))
        polynomialBruteForce = polynomial_brute_force_timeComplexity(A, 10, 100)
        polynomialBruteList.append(polynomialBruteForce)

    for item in polynomialBruteList:
        print(f"Average Polynomials Sum Brute Force runtime: {item}")

    #5
    for l in range(3):
        B = list(range(1, poly_InputSizeB[l]))
        polynomialHorners = polynomial_horners_timeComplexity(B, x, 10)
        polynomialHornersT.append(polynomialHorners)

    for hornerT in polynomialHornersT:
        print(f"Average Polynomials Sum Horner Method runtime: {hornerT}")

    # Graph power function using brute force
    # Plot each graph in a separate figure
    plt.figure(1)
    plt.plot(input_size, listPowerBrute)
    plt.xlabel('Input Size (n)')
    plt.ylabel('Run Time (s)')
    plt.title('Exponentiation Brute Force Method')

    plt.figure(2)
    plt.plot(input_size, listPowerIterative)
    plt.xlabel('Input Size (n)')
    plt.ylabel('Run Time (s)')
    plt.title('Exponentiation Iterative Method')

    plt.figure(3)
    plt.plot(recursive_size, recursiveList)
    plt.xlabel('Input Size (n)')
    plt.ylabel('Run Time (s)')
    plt.title('Exponentiation Recursive Method')

    plt.figure(4)
    plt.plot(poly_InputSizeA, polynomialBruteList)
    plt.xlabel('Input Size (n)')
    plt.ylabel('Run Time (s)')
    plt.title('Polynomial Sum Brute Force Method')

    plt.figure(5)
    plt.plot(poly_InputSizeB, polynomialHornersT)
    plt.xlabel('Input Size (n)')
    plt.ylabel('Run Time (s)')
    plt.title('Polynomial Sum Horners Method')

    plt.show()

if __name__ == "__main__":
    main()