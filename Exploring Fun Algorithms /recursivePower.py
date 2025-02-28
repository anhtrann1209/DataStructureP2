def recursivePower(x, n):
    
    if n == 1:
       return x
    if n == 0:
       return 1

    if n % 2 == 0:
       # meaning it can modulus even power
       results = recursivePower(x, n//2) * recursivePower(x, n//2)

    
    if n % 2 == 1:
       # meaning it an odd power
       results = x * recursivePower(x, n//2) * recursivePower(x, n//2)
    
    return results
    


def main():
  x = 5
  n = 8

  results = recursivePower(x,n)
  print(results)

if __name__ == "__main__":
  main()