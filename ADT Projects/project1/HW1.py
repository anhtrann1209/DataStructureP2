from HW1_Utils import raiseNotDefined

'''
Homework 1 - Calculating Powers and Polynomials
Name: Anh Tran
Date: January 10, 2025
Collaborators: None
'''

# Q1a
def power_brute_force(x, n):
    '''
    Calculate x^n using brute force
    Return the result
    '''
    # Check if inputs n and x value is an integer and greater than 0.
    if not isinstance(n, int) or n < 0 or not isinstance(x, int):
        return None

    if x == 0 and n == 0:
        return 1  # Handle 0^0 as 1.

    result = 1
    for i in range(n):
        result *= x
    return result

# Q1b
def power_iterative(x, n):
    '''
    Calculate x^n using iterative Exponentiation by Squaring
    Return the result
    '''
    if not isinstance(n, int) or n < 0 or not isinstance(x, (int, float)):
        return None  # Return None for improper input

    if x == 0 and n == 0:
        return 1  # Define 0^0 as 1 for consistency

    result = 1
    base = x  # Start with the base value
    while n > 0:
        if n % 2 == 1:  # If the current power is odd
            result *= base  # Multiply result by the base
        base *= base  # Square the base
        n //= 2  # Halve the exponent (integer division)
    return result

# Q1c
def power_recursive(x, n):
    '''
    Calculate x^n using recursive DAC
    Return the result
    '''
    #O(log(n))
    # If power is not an integer
    if not isinstance(n, int) or n < 0 or not isinstance(x, int):
        return None  # Return None for improper input

    # Base cases
    if n == 0:
        return 1
    if n == 1:
        return x

    # If n power divisible by 2 
    if n % 2 == 0:
        result = power_recursive(x, n // 2)
        # Split power by half, and combine x * x
        return result * result
    else:
        # else odd power take out an x
        result = power_recursive(x, n // 2)
        return x * result * result

# Q2a
def polynomial_brute_force(A, x):
    '''
    Calculate the polynomial sum using brute force
    A: list of coefficients
    x: the value to evaluate the polynomial at
    Return the result
    '''
    if not isinstance(A, list) or A is None:
        return None  # If the list is empty return None
    
    # Test case if list empty, return 0.
    if len(A) == 0:
        return 0
    if not isinstance(x, (int, float)): 
        return None  # Return None if x is not a number

    result = 0
    # O(n)
    for i in range(len(A)):
        # Check each values in the list
        if not isinstance(A[i], (int, float)):  
            return None
        # Use power brute force multiply for coefficients
        # O(n)
        result += A[i] * power_brute_force(x, i)  
    return result


# Q2b
def polynomial_horners(A, x):
    '''
    Calculate the polynomial sum using Horner's rule
    A: list of coefficients
    x: the value to evaluate the polynomial at
    Return the result
    '''
    # Equation equation(2), p(x) = a0 + x(a1+x(a3+...+x(an-1 + xan)...))).

    # Check if A is a valid list
    if not isinstance(A, list) or A is None:
        return None  # Return None if it not a proper list.
    
    # Similarlly, return 0 if list is empty
    if len(A) == 0:
        return 0
    
    if not isinstance(x, (int, float)): 
        return None  # Return None if x not int or float.

    result = 0
    #O(n)
    for c in reversed(A):
        # Check if coefficient is int or float
        if not isinstance(c, (int, float)):  
            return None
        result = c + x * result
    return result