def karatsuba_decimal(x: float, y: float) -> float:
    # Split every integers at the decimal
    scale_x = len(str(x).split(".")[1]) if "." in str(x) else 0
    scale_y = len(str(y).split(".")[1]) if "." in str(y) else 0
    
    # use max to keep precision? 
    # 10 to the power of?
    scale_factor = 10 ** max(scale_x, scale_y)
    
    X_int = int(x * scale_factor) # convert to integers
    Y_int = int(y * scale_factor) # convert to integers
    
    # Perform Karatsuba multiplication on integers
    result_int = karatsuba(X_int, Y_int)
    # Scale back to decimal
    return result_int / (scale_factor ** 2)

def karatsuba(x: int, y: int) -> int:
    # Base case for small numbers
    if x < 10 or y < 10:
        return x * y
    
    # Determine size of numbers
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    
    # Split the numbers
    x_H = x // (10 ** m)
    x_L = x % (10 ** m)
    y_H = y // (10 ** m)
    y_L = y % (10 ** m)
    
    # Recursive Karatsuba steps
    P1 = karatsuba(x_H, y_H)
    P2 = karatsuba(x_L, y_L)
    P3 = karatsuba(x_H + x_L, y_H + y_L)
    
    # Compute result using Karatsuba formula
    return P1 * (10 ** (2 * m)) + (P3 - P1 - P2) * (10 ** m) + P2

# Example usage
x = 12.53
y = 1.35
result = karatsuba_decimal(x, y)
print(f"{x} * {y} = {result}")
