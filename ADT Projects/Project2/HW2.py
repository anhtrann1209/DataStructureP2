from HW2_Utils import raiseNotDefined

'''
Programming Project 2 - Sorting
Name: Anh Tran
Date: January 13, 2025
Collaborators: None
'''

# Q1
def insertion_sort(A):
    '''
    Sort the list A in non-decreasing order using the insertion sort algorithm
    A: a list of integers
    Return the sorted list
    '''
    '''A simple insertion sort implementation for demonstration'''

    if not isinstance(A, list):
        return None # not a list
    
    if len(A) == 1 or len(A) == 0:
        return A # Since the list only have one case.
    

    for i in range(1, len(A)):
        # Check each element at i
        if not isinstance(A[i], (int,float)):
            return None
        key = A[i]
        j = i - 1
        while j >= 0 and key < A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
    return A

# Q2a
def merge_sort(A, l, r):
    '''
    Sort the list A in non-decreasing order using the merge sort algorithm
    A: a list of integers
    l: the index of the first element in A
    r: the index of the last element in A
    Return the sorted list
    Run time analysis: T(n) = c + cn + T(n/2) + T(n/2)
    '''

    if not isinstance(l, int) and not isinstance(r, int):
        return None
    if not isinstance(A, list):
        return None
    # If there is only one element
    if len(A) == 0 or len(A) == 1:
        return A
    
    if l < r:
        q = (l + r) // 2
        merge_sort(A, l, q)
        merge_sort(A, q + 1, r)
        merge(A, l, q, r)
    # Else l == r return list A
    return A 

# Q2b
def merge(A, l, m, r):
    '''
    Merge two sorted lists A[p:q] and A[q+1:r]
    A: a list of integers
    l: the index of the first element in A
    m: the index of the middle element in A
    r: the index of the last element in A
    '''
    # Merge function is call from merge sort, list, l & r has checked.
    n1 = m - l + 1
    n2 = r - m

    # Create two new array to stores two sets elements use to compares.
    left = []
    right = []

    # Loop copy data from the left side of array A
    # Check values accuracy at this loop before appending
    for i in range(n1):
        if not isinstance(A[l+i], (int, float)):
            return None
        left.append(A[l + i])
    
    # Loop copy data from the left side of array B
    for j in range(n2):
        if not isinstance(A[m+1+j], (int, float)):
            return None
        right.append(A[m + 1 + j]) # m is q

    i,j = 0,0
    k = l 

    # Combine the elements into the original array
    # While a loops allow easier increment using i,j
    while i < n1 and j < n2:
        # if element from left array is less than element from the right
        if left[i] <= right[j]:
            # append left element
            A[k] = left[i]
            i += 1 #increment i pos
        else:
            A[k] = right[j] # right is less than
            j += 1 # increment j pos
        k += 1 # increment l

    # The remaining elements in the left
    while i < n1:
        A[k] = left[i]
        i += 1
        k += 1 # shift pos by +1

    # The remaining elements on the right 
    while j < n2:
        A[k] = right[j]
        j += 1
        k += 1


def main():
    array = [9, 6, 11, 30, 12, 4, 2]
    
    # Use the same array but copy it, do not modify same memory list.

    #1 Merge sort
    sortMerge = merge_sort(array.copy(), 0 , len(array)-1)  
    print(f"Merge Sort: {sortMerge}")
    
    #2 Insertion sort
    inserttionSort = insertion_sort([9, 6, 11, 30, 12, 4, 2])
    print(f"Insertion Sort: {inserttionSort}")

if __name__ == "__main__":
    main()