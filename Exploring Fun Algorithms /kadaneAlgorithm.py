def kadane_MaxSubSum(A):
  # implement index tracking
  maxSumSoFar = 0 # maximum sub-array
  maxSumTok = 0 # max sum ending at k

  for k in range(len(A)):
    maxSumTok = maxSumTok + A[k] # add the value to total sum
    if maxSumTok < 0: # less than 0
      maxSumTok = 0 #reset the value to 0
      tempStartArrayIndex = k+1 # update starting index
    if maxSumSoFar < maxSumTok:
      maxSumSoFar = maxSumTok
      startArrayIndex = tempStartArrayIndex  # update starting index for different cases
      finalArrayIndex = k # final index is where the loop stop for the condition

  return [startArrayIndex, finalArrayIndex], maxSumSoFar

def main():
    array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    indices, max_sum = kadane_MaxSubSum(array)
    print(f"Maximum Subarray: {array[indices[0]:indices[1] + 1]}")
    print(f"Indices: {indices}")
    print(f"Maximum Sum: {max_sum}")


if __name__ == "__main__":
    main()

"""
PSEUDOCODE:

KADANE_MaxSubSum(A):
  maxSumSoFar = 0
  maxSumTok = 0 
  for k=1 to n
    maxSumTok = maxSumTok + A[k]
    if maxSumTok < 0
      maxSumTok = 0
      tempStartIndex = k+1
    if maxSumSoFar < maxSumTok
      maxSumSoFar = maxSumTok
      startArrayIndex = tempStartIndex
      finalArrayIndex = k
  
  Return [startArrayIndex, finalArrayIndex], maxSumSoFar
"""